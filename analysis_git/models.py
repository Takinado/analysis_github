"""Модели для анализа репозитория GitHub"""
import datetime
import json

from utils import get_response, check_message_from_github

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class Repository:
    """Репозиторий"""

    def __init__(
        self, path: str, since: str = '', until: str = '', branch: str = 'master', token: str = ''
    ):
        self.path = path
        self.since = since
        self.until = until
        self.branch = branch
        self.token = token
        self.commits = []
        self.pulls = []
        self.issues = []

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.path}>'

    def load_commits(self) -> list:
        """Запрашиваем репозиторий и формируем список коммитов"""
        params = {
            'since': self.since,
            'until': self.until,
            'sha': self.branch,
            'per_page': 100,
        }
        result = self._get_data(Commit, self.path + '/commits', params)
        self.commits = result
        return result

    def _get_data(self, cls, url: str, params: dict = None) -> list:
        """Получить данные с репозитория и получить список объектов заданного класса"""
        result = []
        r = get_response(url, self.token, params)
        answer = json.loads(r.text)
        check_message_from_github(answer)
        for raw_commit in answer:
            result.append(cls(raw_commit))
        if r.links.get('next'):
            result += self._get_data(cls, r.links['next']['url'])
        return result

    def commit_authors(self) -> list:
        """Анализ авторов коммитов"""
        counted_commit_authors = {}
        for commit in self.commits:
            if commit.author_login in counted_commit_authors:
                counted_commit_authors[commit.author_login] += 1
            else:
                counted_commit_authors[commit.author_login] = 1

        counted_commit_authors = list(counted_commit_authors.items())
        counted_commit_authors.sort(key=lambda i: i[1])
        counted_commit_authors.reverse()
        return counted_commit_authors[:30]

    def load_pulls(self) -> list:
        """Запрашиваем репозиторий и формируем список pull requests"""
        params = {
            'state': 'all',
            'base': self.branch,
        }
        result = self._get_data(Pull, self.path + '/pulls', params)
        result = list(filter(lambda pull: pull.in_date_range(self.since, self.until), result))
        self.pulls = result
        return result

    def load_issues(self) -> list:
        """Запрашиваем репозиторий и формируем список issues"""
        params = {
            'filter': 'all',
            'state': 'all',
            'since': self.since,
        }
        self.issues = self._get_data(Issue, self.path + '/issues', params)
        return self.issues

    @staticmethod
    def count_open(events) -> int:
        return len(list(filter(lambda event: event.is_open(), events)))

    @staticmethod
    def count_closed(events) -> int:
        return len(list(filter(lambda event: event.is_closed(), events)))

    @staticmethod
    def count_old(events) -> int:
        return len(list(filter(lambda event: event.is_old(), events)))

    def print_top_authors(self):
        for author in self.commit_authors():
            print(author[0], ':', author[1])
        print('\n')

    def print_counted_pulls(self):
        print(f"Open pull requests: {self.count_open(self.pulls)}")
        print(f"Closed pull requests: {self.count_closed(self.pulls)}")

    def print_old_pulls(self):
        print(f"Old pull requests: {self.count_old(self.pulls)}\n")

    def print_counted_issues(self):
        print(f"Open issues: {self.count_open(self.issues)}")
        print(f"Closed issues: {self.count_closed(self.issues)}")

    def print_old_issues(self):
        print(f"Old issues: {self.count_old(self.issues)}\n")


class Commit:
    def __init__(self, raw_commit):
        self.sha = raw_commit.get('sha')
        self.author_login = raw_commit['author'].get('login') if raw_commit.get('author') else None

    def __repr__(self):
        return '<Commit: {}>'.format(self.sha)


class Event:
    """ Абстрактный класс для pull_request и issue"""

    def __init__(self, raw_data: dict):
        self.number = raw_data.get('number')
        self.state = raw_data.get('state')
        self.created_at = datetime.datetime.strptime(raw_data.get('created_at'), DATETIME_FORMAT)

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.number}>'

    def is_open(self):
        if self.state == 'open':
            return True

    def is_closed(self):
        if self.state == 'closed':
            return True


class Pull(Event):
    """Pull request"""

    def is_old(self):
        if self.state == 'open' and (
            self.created_at < datetime.datetime.now() + datetime.timedelta(days=-30)
        ):
            return True

    def in_date_range(self, since, until):
        start_date = datetime.datetime.strptime(since, DATETIME_FORMAT) if since else None
        end_date = datetime.datetime.strptime(until, DATETIME_FORMAT) if until else None
        if start_date and (start_date > self.created_at):
            return False
        if end_date and (self.created_at > end_date):
            return False
        return True


class Issue(Event):
    def __init__(self, raw_data):
        super().__init__(raw_data)
        raw_closed_at = raw_data.get('closed_at')
        self.closed_at = (
            datetime.datetime.strptime(raw_closed_at, DATETIME_FORMAT) if raw_closed_at else None
        )

    def is_old(self):
        if self.state == 'open' and (
            self.created_at < datetime.datetime.now() + datetime.timedelta(days=-14)
        ):
            return True
        if self.state == 'closed' and (
            self.created_at < self.closed_at + datetime.timedelta(days=-14)
        ):
            return True
        return False

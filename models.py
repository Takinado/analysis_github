import datetime
import json


from analysis import get_response, check_message_from_github

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class Repository:
    """Репозиторий"""

    def __init__(self, path: str, since: str, until: str, branch: str):
        self.path = path
        self.since = since
        self.until = until
        self.branch = branch
        self.commits = []
        self.pulls = []

    def load_commits(self) -> list:
        """Запрашиваем репозиторий и формируем список коммитов"""
        params = {
            'since': self.since,
            'until': self.until,
            'sha': self.branch,
            'per_page': 100,
        }
        result = self._get_commits(self.path + '/commits', params=params)
        self.commits = result
        return result

    def _get_commits(self, url: str, params: dict = None) -> list:
        result = []
        r = get_response(url, params)
        answer = json.loads(r.text)
        check_message_from_github(answer)
        for raw_commit in answer:
            result.append(Commit(raw_commit))
        if r.links.get('next'):
            result += self._get_commits(r.links['next']['url'])
        return result

    def load_pulls(self) -> list:
        """Запрашиваем репозиторий и формируем список pull requests"""
        params = {
            'state': 'all',
            'base': self.branch,
        }
        result = self._get_pulls(self.path + '/pulls', params=params)
        result = list(filter(lambda pull: pull.in_date_range(self.since, self.until), result))
        self.pulls = result
        return result

    def _get_pulls(self, url: str, params: dict = None) -> list:
        result = []
        r = get_response(url, params)
        answer = json.loads(r.text)
        check_message_from_github(answer)
        for raw_pull in answer:
            result.append(Pull(raw_pull))
        # TODO commented for test
        # if r.links.get('next'):
        #     result += self._get_pulls(r.links['next']['url'])
        return result

    def count_open_pulls(self) -> int:
        open_pulls = list(filter(lambda pull: pull.is_open(), self.pulls))
        return len(open_pulls)

    def count_closed_pulls(self) -> int:
        closed_pulls = list(filter(lambda pull: pull.is_closed(), self.pulls))
        return len(closed_pulls)

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

    def print_top_authors(self):
        self.load_commits()
        for author in self.commit_authors():
            print(author[0], ':', author[1])

    def print_counted_pulls(self):
        self.load_pulls()
        print(f"Open pull requests: {self.count_open_pulls()}")
        print(f"Closed pull requests: {self.count_closed_pulls()}")

    def __repr__(self):
        return '<Repository: {}>'.format(self.path)


class Commit:
    def __init__(self, raw_commit):
        self.sha = raw_commit.get('sha')
        self.author_login = raw_commit['author'].get('login') if raw_commit.get('author') else None

    def __repr__(self):
        return '<Commit: {}>'.format(self.sha)


class Pull:
    """Pull request"""
    def __init__(self, raw_pull_request: dict):
        self.number = raw_pull_request.get('number')
        self.state = raw_pull_request.get('state')
        self.created_at = datetime.datetime.strptime(raw_pull_request.get('created_at'), DATETIME_FORMAT)

    def is_open(self):
        if self.state == 'open':
            return True

    def is_closed(self):
        if self.state == 'closed':
            return True

    def in_date_range(self, since, until):
        start_date = datetime.datetime.strptime(since, DATETIME_FORMAT) if since else None
        end_date = datetime.datetime.strptime(until, DATETIME_FORMAT) if until else None
        if start_date and (start_date > self.created_at):
            return False
        if end_date and (self.created_at > end_date):
            return False
        return True

    def __repr__(self):
        return '<Pull: {}>'.format(self.number)

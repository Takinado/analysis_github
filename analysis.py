"""Скрипт анализа репозитория GitHub"""
import json
import logging
import requests
import sys

from urllib3.exceptions import MaxRetryError

logger = logging.getLogger(__name__)


def get_params() -> dict:
    """Получение параметров скрипта"""
    params = {}
    if len(sys.argv) == 1:
        logger.error('Error. Specify a repository')
        sys.exit(1)
    params['repository'] = sys.argv[1]
    params['repository'] = params['repository'].replace('https://github.com/', 'https://api.github.com/repos/')
    params['branch'] = 'master'
    return params


def get_author_logins(commits: list) -> list:
    """Получить логины авторов
    >>> get_author_logins([{'author': {'login': 'a'}}, {'author': {'login': 'a'}}, {'author': None}])
    ['a', 'a']
    """
    logins = []
    for commit in commits:
        if commit['author']:
            logins.append(commit['author'].get('login'))
    return logins


def get_commit_authors(url: str) -> list:
    """Получение авторов коммитов"""
    print(f'Request page {url}')
    try:
        r = requests.get(url)
    except MaxRetryError as e:
        logger.error(e.reason)
        sys.exit(1)
    answer = json.loads(r.text)
    if type(answer) == dict and answer.get('message'):
        logger.error(answer['message'])
        sys.exit(1)
    commit_authors = get_author_logins(answer)
    if r.links.get('next'):
        commit_authors += get_commit_authors(r.links['next']['url'])
    return commit_authors


def analysis_commit_authors(commit_authors: list) -> list:
    """Анализ авторов коммитов
    >>> analysis_commit_authors(['a', 'b', 'b'])
    [('b', 2), ('a', 1)]
    """
    counted_commit_authors = {}
    for author in commit_authors:
        if author in counted_commit_authors:
            counted_commit_authors[author] += 1
        else:
            counted_commit_authors[author] = 1
    counted_commit_authors = list(counted_commit_authors.items())
    counted_commit_authors.sort(key=lambda i: i[1])
    counted_commit_authors.reverse()
    return counted_commit_authors[:30]


def analyze(params: dict):
    """Анализ репозитория"""
    # print TOP of authors
    commit_authors = get_commit_authors(f"{params['repository']}/commits")
    for author in analysis_commit_authors(commit_authors):
        print(author[0], ':', author[1])


if __name__ == '__main__':
    params = get_params()
    analyze(params)

"""Скрипт анализа репозитория GitHub"""
import argparse
import calendar
import json
import logging
import requests
import time
import sys

from urllib3.exceptions import MaxRetryError

# Create a custom logger
logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('analysis.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
logger.addHandler(c_handler)
logger.addHandler(f_handler)


# def get_params() -> dict:
#     """Получение параметров скрипта"""
#     params = {}
#     if len(sys.argv) == 1:
#         logger.error('Error. Specify a repository')
#         sys.exit(1)
#     repository = sys.argv[1]
#     params['repository'] = repository.replace('https://github.com/', 'https://api.github.com/repos/')
#     if params['repository'] == repository:
#         logger.error('Error in repository path')
#         sys.exit(1)
#     params['branch'] = 'master'
#     return params

def get_params() -> argparse.Namespace:
    """Получение параметров скрипта"""

    parser = argparse.ArgumentParser()
    parser.add_argument('repository', help='Full path to repository (https://github.com/...)')
    parser.add_argument('-s', '--since', help='Only data after this date will be analyze. '
                                              'This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    parser.add_argument('-u', '--until', help='Only data before this date will be analyze. '
                                              'This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    parser.add_argument('-b', '--branch', help='Repository branch. Default: master')

    args = parser.parse_args()
    if not args.branch:
        args.branch = 'master'
    repository = args.repository.replace('https://github.com/', 'https://api.github.com/repos/')
    if args.repository == repository:
        logger.error('Error in repository path')
        sys.exit(1)
    else:
        args.repository = repository
    return args


def check_message_from_github(answer):
    """Проверяем не вернул ли GitHub ошибку"""
    if type(answer) == dict and answer.get('message'):
        logger.error(answer['message'])
        sys.exit(1)


def request_response(url: str, params=None):
    """Получить response с репозитория"""
    try:
        r = requests.get(url, params)
    except MaxRetryError as e:
        logger.error(e.reason)
        sys.exit(1)
    return r


def get_response(url: str, params=None):
    """Получить response с учетом задержки по лимитам"""
    r = request_response(url, params)
    while r.headers._store['x-ratelimit-remaining'][1] == '0':
        reset_timestamp = int(r.headers._store['x-ratelimit-reset'][1])
        sleep_time = reset_timestamp - calendar.timegm(
            time.gmtime()) + 5  # add 5 seconds to be sure the rate limit has been reset
        logger.warning(f"Activate sleep mode to {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_timestamp))}")
        time.sleep(sleep_time)
        r = request_response(url, params)
    return r


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


def get_commit_authors(url: str, params=None) -> list:
    """Получение авторов коммитов"""
    r = get_response(url, params)
    answer = json.loads(r.text)
    check_message_from_github(answer)
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


def get_pull_requests(url: str) -> int:
    """Получение pull requests"""
    r = get_response(url)
    answer = json.loads(r.text)
    check_message_from_github(answer)
    pull_requests = len(answer)
    if r.links.get('next'):
        pull_requests += get_pull_requests(r.links['next']['url'])
    return pull_requests


def analyze(args: argparse.Namespace):
    """Анализ репозитория"""
    # print TOP of authors
    params = {
        'since': args.since,
        'until': args.until,
        'sha': args.branch,
    }

    commit_authors = get_commit_authors(args.repository + '/commits', params=params)
    for author in analysis_commit_authors(commit_authors):
        print(author[0], ':', author[1])

    # Count pull requests
    open_pull_url = f"{params['repository']}/pulls?state=open"
    print(f"Open pull requests: {get_pull_requests(open_pull_url)}")
    closed_pull_url = f"{params['repository']}/pulls?state=closed"
    print(f"Closed pull requests: {get_pull_requests(closed_pull_url)}")


if __name__ == '__main__':
    args = get_params()
    analyze(args)

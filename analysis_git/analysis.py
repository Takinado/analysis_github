"""Скрипт анализа репозитория GitHub"""
import argparse
import calendar
import logging
import requests
import time
import sys


DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

# Create a custom logger
logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

f_handler = logging.FileHandler('../analysis.log')
f_handler.setLevel(logging.ERROR)
f_format = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

work_handler = logging.FileHandler('../work.log')
work_handler.setLevel(logging.INFO)
work_handler.setFormatter(f_format)
logger.addHandler(work_handler)


def get_params() -> argparse.Namespace:
    """Получение параметров скрипта"""

    parser = argparse.ArgumentParser()
    parser.add_argument('repository', help='Full path to repository (https://github.com/...)')
    parser.add_argument('-s', '--since', help='Only data after this date will be analyze. '
                                              'This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    parser.add_argument('-u', '--until', help='Only data before this date will be analyze. '
                                              'This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    parser.add_argument('-b', '--branch', help='Repository branch. Default: master')
    parser.add_argument('-t', '--token', help='GitHub OAuth2 token (use to increase rate limit)')

    args = parser.parse_args()
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


def request_response(url: str, token: str = None, params: dict = None):
    """Получить response с репозитория"""
    headers = {'Authorization': f'token {token}'} if token else {}
    try:
        r = requests.get(url, params=params, headers=headers)
    except Exception as error:
        logger.error(f'{error}')
        sys.exit(1)
    # logger.info(f"{url} downloaded. Rate limit {r.headers._store['x-ratelimit-remaining'][1]}")
    # logger.warning(f"{url} downloaded. Rate limit {r.headers._store['x-ratelimit-remaining'][1]}")
    return r


def get_response(url: str, token: str = None, params: dict = None):
    """Получить response с учетом задержки по лимитам"""
    r = request_response(url, token, params)
    while r.headers._store['x-ratelimit-remaining'][1] == '0':
        reset_timestamp = int(r.headers._store['x-ratelimit-reset'][1])
        sleep_time = reset_timestamp - calendar.timegm(
            time.gmtime()) + 5  # add 5 seconds to be sure the rate limit has been reset
        logger.warning(f"Activate sleep mode to {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_timestamp))}")
        time.sleep(sleep_time)
        r = request_response(url, token, params)
    return r


def analyze():
    """Анализ репозитория"""
    args = get_params()
    params = {
        'since': args.since,
        'until': args.until,
        'branch': args.branch,
        'token': args.token,
    }

    from models import Repository
    repository = Repository(args.repository, **params)

    repository.load_commits()
    repository.print_top_authors()

    repository.load_pulls()
    repository.print_counted_pulls()
    repository.print_old_pulls()

    repository.load_issues()
    repository.print_counted_issues()
    repository.print_old_issues()


if __name__ == '__main__':
    analyze()

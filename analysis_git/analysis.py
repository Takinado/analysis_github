"""Скрипт анализа репозитория GitHub"""
import argparse
import sys
from models import Repository


def get_params() -> argparse.Namespace:
    """Получение параметров скрипта"""

    parser = argparse.ArgumentParser()
    parser.add_argument('repository', help='Full path to repository (https://github.com/...)')
    parser.add_argument(
        '-s',
        '--since',
        help='Only data after this date will be analyze. '
        'This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.',
    )
    parser.add_argument(
        '-u',
        '--until',
        help='Only data before this date will be analyze. '
        'This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.',
    )
    parser.add_argument('-b', '--branch', help='Repository branch. Default: master')
    parser.add_argument('-t', '--token', help='GitHub OAuth2 token (use to increase rate limit)')

    args = parser.parse_args()
    repository = args.repository.replace('https://github.com/', 'https://api.github.com/repos/')
    if args.repository == repository:
        print('Error in repository path')
        sys.exit(1)
    else:
        args.repository = repository
    return args


def analyze():
    """Анализ репозитория"""
    args = get_params()
    params = {
        'since': args.since,
        'until': args.until,
        'branch': args.branch,
        'token': args.token,
    }

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

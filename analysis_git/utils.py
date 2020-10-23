"""Утилиты для анализа репозитория GitHub"""
import calendar
import logging
import time
import sys
import requests


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


def get_response(url: str, token: str = None, params: dict = None):
    """Получить response с учетом задержки по лимитам"""
    result = request_response(url, token, params)
    while result.headers._store['x-ratelimit-remaining'][1] == '0':
        reset_timestamp = int(result.headers._store['x-ratelimit-reset'][1])
        sleep_time = (
            reset_timestamp - calendar.timegm(time.gmtime()) + 5
        )  # add 5 seconds to be sure the rate limit has been reset
        reset_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_timestamp))
        logger.warning(f'Activate sleep mode to {reset_time}')
        time.sleep(sleep_time)
        result = request_response(url, token, params)
    return result


def check_message_from_github(answer):
    """Проверяем не вернул ли GitHub ошибку"""
    if isinstance(answer, dict) and answer.get('message'):
        logger.error(answer['message'])
        sys.exit(1)


def request_response(url: str, token: str = None, params: dict = None):
    """Получить response с репозитория"""
    headers = {'Authorization': f'token {token}'} if token else {}
    try:
        result = requests.get(url, params=params, headers=headers)
    except Exception as error:
        logger.error(f'{error}')
        sys.exit(1)
    return result

import re

POSSIBLE_DATE_REGEX = re.compile(r'''
    (0?[1-9]|[12][0-9]|3[01])
    (?P<sep>\-|/)
    (0?[1-9]|1[012])
    (?P=sep)
    (\d{4})
''', re.VERBOSE)
# https://docs-python.ru/tutorial/ispolzovanie-reguljarnyh-vyrazhenij-python/imenovannye-gruppy-reguljarnyh-vyrazhenijah/


def check_date(date):
    day, month, year = map(int, re.compile('[/-]').split(date))
    if 12 < month or year < 1000 or 2999 < year:
        return False
    if month in (4, 6, 9, 11):
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= (29 if is_leap_year(year) else 28)
    return 1 <= day <= 31


def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def normalize_date(date):
    day, month, year = map(int, re.compile('[/-]').split(date))
    return f'{day:02d}/{month:02d}/{year}'


def get_date_tokens(match_result):
    day, _, month, year = match_result
    return (day, month, year)


def get_date(match):
    day, _, month, year = match
    return f"{day}/{month}/{year}"

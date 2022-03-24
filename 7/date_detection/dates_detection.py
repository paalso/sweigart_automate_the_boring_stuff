#!/usr/bin/env python3

# https://automatetheboringstuff.com/2e/chapter7/

# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999. Note that if the day or month is a
# single digit, it’ll have a leading zero.


import re
import sys

POSSIBLE_DATE_REGEX = re.compile(r'''
    (0?[1-9]|[12][0-9]|3[01])
    (\-|/)
    (0?[1-9]|1[012])
    \2
    (\d{4})
''', re.VERBOSE)


def normalize_date(date_tokens):
    day, month, year = map(int, date_tokens)
    return f'{day:02d}/{month:02d}/{year}'


def check_date(date_tokens):
    day, month, year = map(int, date_tokens)
    if year < 1000 or 2999 < year:
        return False
    if month in (4, 6, 9, 11):
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= (29 if is_leap_year(year) else 28)
    return 1 <= day <= 31


def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def upd_date_tokens(date_tokens, match_results):
    date_tokens.extend(
        map(normalize_date,
            filter(check_date,
                   map(get_date_tokens, match_results))))


def get_date_tokens(match_result):
    day, _, month, year = match_result
    return (day, month, year)


def parse_args():
    if len(sys.argv) != 2:
        print('Usage: {sys.argv[0]} filename')
        sys.exit(1)
    return sys.argv[1]


def main():
    filename = parse_args()
    all_dates = []
    with open(filename, 'r') as f:
        for line in f:
            upd_date_tokens(all_dates, POSSIBLE_DATE_REGEX.findall(line))

    print(*all_dates, sep="\n")


if __name__ == '__main__':
    main()
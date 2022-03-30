#!/usr/bin/env python3

# https://automatetheboringstuff.com/2e/chapter7/

# Dates Normalization

import sys
import re

POSSIBLE_DATE_REGEX = re.compile(r'''(?P<date>
    ((0?[1-9]|[12][0-9]|3[01])
    (?P<sep1>[/-])
    (0?[1-9]|1[012])
    (?P=sep1)
    (\d{4}))|
    (
    (\d{4})
    (?P<sep2>[/-])
    (0?[1-9]|[12][0-9]|3[01])
    (?P=sep2)
    (0?[1-9]|1[012])))
''', re.VERBOSE)


POSSIBLE_DATE_REGEX = re.compile(r'''(?P<date>
    \b((0?[1-9]|[12][0-9]|3[01])
    (?P<sep1>[/-])
    (0?[1-9]|1[012])
    (?P=sep1)
    (\d{4}))|
    (
    (\d{4})
    (?P<sep2>[/-])
    (0?[1-9]|1[012])
    (?P=sep2)
    (0?[1-9]|[12][0-9]|3[01])))\b
''', re.VERBOSE)


def parse_args():
    if len(sys.argv) != 2:
        print('Usage: {sys.argv[0]} filename')
        sys.exit(1)
    return sys.argv[1]


def generate_fixed_filename(filename, suffix):
    return f'{filename}-{suffix}'


def normalize_date(date):
    tokens = re.compile('[/-]').split(date)
    if len(tokens[0]) == 4:
        year, month, day = tokens
    else:
        day, month, year = tokens
    day = day.rjust(2, '0')
    month = month.rjust(2, '0')
    return f'{day}/{month}/{year}'


def check_date(date):
    day, month, year = map(int, date.split('/'))
    if 12 < month or year < 1000 or 2999 < year:
        return False
    if month in (4, 6, 9, 11):
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= (29 if is_leap_year(year) else 28)
    return 1 <= day <= 31


def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def normalize_dates(regex, filename):
    normalized_filename = generate_fixed_filename(filename, 'FIXED')
    with open(filename, 'r') as f_in, open(normalized_filename, 'w') as f_out:
        for line in f_in:
            possible_dates = map(lambda e: e[0], regex.findall(line))
            possible_to_normalized_dates_dict = {
                date: normalize_date(date) for date in possible_dates
            }
            for possible_date, normalized_date in \
                    possible_to_normalized_dates_dict.items():
                if check_date(normalized_date):
                    print(f'replacing {possible_date} -> {normalized_date}')
                    line = line.replace(possible_date, normalized_date)
                else:
                    print(f'skipping {possible_date}')
            f_out.write(line)


def main():
    filename = parse_args()
    normalize_dates(POSSIBLE_DATE_REGEX, filename)


if __name__ == '__main__':
    main()

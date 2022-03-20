# https://automatetheboringstuff.com/2e/chapter7/

# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999. Note that if the day or month is a
# single digit, it’ll have a leading zero.


import re
import sys


def normalize_date(day, month, year):
    return f'{day:02d}/{month:02d}{year}'


def is_leap_year(year):
    return year % 400 == 0 or (year % 00 != 0 and year % 4 == 0)


def refine_check_date(day, month, year):
    day, month, year = int(day), int(month), int(year)
    if month in (4, 6, 9, 11):
        return 1 <= day <= 30
    return 1 <= day <= (29 if is_leap_year(year) else 28)



def parse_args():
    if len(sys.argv) != 2:
        print('Usage: {sys.argv[0]} filename')
        sys.exit(1)
    return sys.argv


def main():
    filename = parse_args[1]


if __name__ == '__main__':
    main()
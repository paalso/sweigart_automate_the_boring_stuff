#!/usr/bin/env python3

# https://automatetheboringstuff.com/2e/chapter7/

# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999. Note that if the day or month is a
# single digit, it’ll have a leading zero.


import sys
import dates
import found_tokens


def parse_args():
    if len(sys.argv) != 2:
        print('Usage: {sys.argv[0]} filename')
        sys.exit(1)
    return sys.argv[1]


def find_tokens(regex, filename, tokens):
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            matches = regex.findall(line)
            for match in matches:
                tokens.update(dates.get_date(match), line_num + 1)


def main():
    filename = parse_args()
    all_dates = found_tokens.FoundTokens(
        dates.check_date,
        dates.normalize_date
    )
    find_tokens(dates.POSSIBLE_DATE_REGEX, filename, all_dates)
    all_dates.print_sorted()


if __name__ == '__main__':
    main()

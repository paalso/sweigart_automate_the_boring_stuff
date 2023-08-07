#!/usr/bin/env python3

'''
rename_dates.py
Renames filenames with American MM-DD-YYYY date format # to European DD-MM-YYYY
'''

import re
import os
import shutil


DATE_PATTERN = re.compile(
    r"""^(.*?)                        # all text before the date
    ((0|1)?\d)-                       # one or two digits for the month
    ((0|1|2|3)?\d)-                   # one or two digits for the day
    ((19|20)\d\d)                     # four digits for the year
    (.*?)$                            # all text after the date
    """, re.VERBOSE)


def check_filename_for_needed_date_style(filename, pattern):
    return pattern.search(filename)


def rename_recomposing_date_format(matching, format='eu'):
    prefix = matching.group(1)
    date_tokens = map(matching.group, (2, 4, 6))
    suffix = matching.group(8)

    if format.lower() == 'eu':
        month, day, year = date_tokens
        new_date_tokens = day, month, year
    elif format.lower() == 'us':
        day, month, year = date_tokens
        new_date_tokens = month, day, year

    new_date_tokens = map(lambda token: token.zfill(2), new_date_tokens)
    return f"{prefix}{'-'.join(new_date_tokens)}{suffix}"


def process_dir(pattern, dirname='.'):
    for filename in os.listdir('.'):
        full_filename = os.path.abspath(filename)
        matching = check_filename_for_needed_date_style(
            filename, pattern)
        if matching:
            new_filename = rename_recomposing_date_format(matching)
            new_full_filename = os.path.abspath(new_filename)
            print(f'renaming {filename} -> {new_filename}')
            shutil.move(full_filename, new_full_filename)


def main():
    process_dir(DATE_PATTERN)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

'''
rename_dates.py
Renames filenames between American MM-DD-YYYY date and European DD-MM-YYYY one
'''

import argparse
import re
import shutil
from pathlib import Path


DATE_PATTERN = re.compile(
    r"""^(.*?)                        # all text before the date
    ((0|1)?\d)-                       # one or two digits for the month
    ((0|1|2|3)?\d)-                   # one or two digits for the day
    ((19|20)\d\d)                     # four digits for the year
    (.*?)$                            # all text after the date
    """, re.VERBOSE)


def get_parser():
    parser = argparse.ArgumentParser(
        description='Renames filenames between American MM-DD-YYYY date' +
                    ' and European DD-MM-YYYY one')

    parser.add_argument('path', nargs='?', default='.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-eu', '--european', action='store_true')
    group.add_argument('-us', '--united_states', action='store_true')

    return parser


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


def get_full_dir_path(filename):
    file_path = Path(filename)
    if Path.is_absolute(file_path):
        return file_path
    return Path.cwd() / filename


def process_dir(pattern, dirpath, format='eu'):
    cwd = Path.cwd()
    for path in Path.iterdir(dirpath):
        filename = path.name
        matching = check_filename_for_needed_date_style(
                    filename, pattern)
        if matching:
            new_filename = rename_recomposing_date_format(matching, format)
            new_path = dirpath / new_filename
            print(f'renaming {path.relative_to(cwd)} -> ' +
                  f'{new_path.relative_to(cwd)}')
            shutil.move(path, new_path)


def main():
    parser = get_parser()
    args = parser.parse_args()
    dirname = args.path
    date_format = 'eu' if args.european else 'us'

    dirpath = get_full_dir_path(dirname)

    if not Path.exists(dirpath):
        print(f'Error: {dirname} does not exist')
        exit(2)

    process_dir(DATE_PATTERN, dirpath, date_format)


if __name__ == '__main__':
    main()

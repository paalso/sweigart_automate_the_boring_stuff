#!/usr/bin/env python3

'''
find_big_files.py

This script searches for large files or folders within a specified directory.
It takes a directory path and a size threshold as input arguments.
It can also include directories in its search if the '-d' or '--dirs_consider'
option is used.

Usage:
    find_big_files.py dir_path size [-d]

Arguments:
    dir_path            The path of the directory in which to search for large
                        files.
    size                The size threshold for identifying large files.
                        The size argument can accept values like '100KB', '2MB',
                        '1GB', etc.
    -d, --dirs_consider Include directories in the search for large items.

Example:
    find_big_files.py /path/to/directory 100MB -d

Note:
    If the directory does not exist, the script will exit with error code 2.
'''

import argparse
import os
import re

DIR_NOT_FOUND_ERROR = 2


def parse_size(size_str):
    size_str = size_str.lower()
    match = re.match(r'^(\d+)([kmgtp]?b?)?$', size_str)
    if not match:
        raise argparse.ArgumentTypeError(f"Invalid size format: {size_str}")

    size = int(match.group(1))
    unit = match.group(2)

    if unit == 'kb':
        size *= 1024
    elif unit == 'mb':
        size *= 1024 ** 2
    elif unit == 'gb':
        size *= 1024 ** 3
    elif unit == 'tb':
        size *= 1024 ** 4
    elif unit == 'pb':
        size *= 1024 ** 5

    return size


def get_parser():
    parser = argparse.ArgumentParser(
        description='Searches for large files or folders')
    parser.add_argument('dir_path', help='The directory path to search')
    parser.add_argument('size', type=parse_size,
                        help='Size threshold for identifying large files. '
                             'Examples: 100KB, 2MB, 1GB, etc.')
    parser.add_argument('-d', '--dirs_consider', action='store_true',
                        help='Include dirs in the search for large items')
    return parser


def check_source_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        print(f'No such directory: {directory_path}')
        exit(DIR_NOT_FOUND_ERROR)
    return True


def get_large_paths_info(directory_path, limit_size, dirs_consider=True):
    large_files = []
    large_dirs = []
    for dirname, subdirs, filenames in os.walk(directory_path):
        if os.path.islink(dirname):
            continue

        if dirs_consider:
            if (size := get_directory_full_size(dirname)) > limit_size:
                large_dirs.append((size, dirname))

        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.islink(full_filename):
                continue
            if (size := os.path.getsize(full_filename)) > limit_size:
                large_files.append((size, full_filename))
    return large_files, large_dirs


def get_directory_full_size(directory_path):
    full_size = 0
    for dirname, subdirs, filenames in os.walk(directory_path,
                                               followlinks=True):
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            # Check if it's not a symbolic link
            if not os.path.islink(full_filename):
                full_size += os.path.getsize(full_filename)
    
    return full_size


def format_number(number):
    return '{:,}'.format(number)


def print_paths_sizes(large_paths_info):
    sorted_info = sorted(large_paths_info, key=lambda pair: -pair[0])

    largest_size = sorted_info[0][0]
    formatted_size = format_number(largest_size)
    size_output_width = len(formatted_size) + 1

    for size, path in sorted_info:
        print(f'{format_number(size):<{size_output_width}}{path}')


def print_results(dir_path, size, dirs_consider):
    large_files_info, large_dirs_info = \
        get_large_paths_info(dir_path, size, dirs_consider)
    if not large_files_info and not large_dirs_info:
        return
    if large_dirs_info:
        print_paths_sizes(large_dirs_info)
        print()

    if large_files_info:
        print_paths_sizes(large_files_info)


def main():
    args = get_parser().parse_args()
    dir_path = args.dir_path
    size = args.size
    dirs_consider = args.dirs_consider

    if check_source_directory_exists(dir_path):
        print_results(dir_path, size, dirs_consider)


if __name__ == '__main__':
    main()

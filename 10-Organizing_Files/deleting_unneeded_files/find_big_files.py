#!/usr/bin/env python3


import argparse
import os
import re


FROM_PATH_NOT_EXISTS = 1


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
    parser.add_argument('from_path')
    parser.add_argument('size', type=parse_size)
    return parser


def check_source_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        print(f'No such directory: {directory_path}')
        exit(os.EX_NOINPUT)
    return True


def get_large_paths_info(directory_path, limit_size):
    large_paths = []
    for dirname, subdirs, filenames in os.walk(directory_path):
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if (size := os.path.getsize(full_filename)) > limit_size:
                large_paths.append((size, full_filename))
    return large_paths


def get_directory_full_size(directory_path):
    full_size = 0
    for dirname, subdirs, filenames in os.walk(directory_path):
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            full_size += os.path.getsize(full_filename)

    return full_size


def print_results(large_paths_info):
    sorted_info = sorted(large_paths_info, key=lambda pair: -pair[0])

    largest_size = sorted_info[0][0]
    size_output_width = len(str(largest_size)) + 1

    for size, path in sorted_info:
        print(f'{size:<{size_output_width}}{path}')


def main():
    args = get_parser().parse_args()
    from_path = args.from_path
    size = args.size

    if check_source_directory_exists(from_path):
        large_paths_info = get_large_paths_info(from_path, size)
        if not large_paths_info:
            return
        print_results(large_paths_info)


if __name__ == '__main__':
    main()

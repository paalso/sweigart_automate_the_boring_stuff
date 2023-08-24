#!/usr/bin/env python3

'''
selective_copy.py

This script allows you to selectively copy files with a specified extension
from one directory to another. It takes two directory paths as arguments,
along with an optional extension parameter. Files in the source directory
that match the specified extension will be copied to the destination directory.

Usage:
    selective_copy.py source_dir destination_dir [-e EXTENSION]

Arguments:
    source_dir      The source directory from which files will be copied.
    destination_dir The destination directory where selected files will be
    copied to.
    -e, --extension Specify the file extension to filter files for copying.

Example:
    selective_copy.py /path/to/source /path/to/destination -e txt

Note:
    If the destination directory doesn't exist, this script will attempt
    to create it.
'''

import argparse
import os
import shutil


FROM_PATH_NOT_EXISTS = 1
TO_PATH_CREATING_ERROR = 2


def get_parser():
    parser = argparse.ArgumentParser(
        description='Copy files with the given extension to a backup dir')
    parser.add_argument('from_path')
    parser.add_argument('to_path')
    parser.add_argument('-e', '--extension', required=True)
    return parser


def check_file(path, extension):
    suffix = os.path.splitext(path)[-1]
    return os.path.isfile(path) and suffix == f'.{extension}'


def copy_files(from_path, to_path, extension):
    for dirname, subdirs, filenames in os.walk(from_path):
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if check_file(full_filename, extension):
                try:
                    print(f'Backuping {full_filename}')
                    shutil.copy(full_filename, to_path)
                except OSError as e:
                    print(f"Error backuping '{full_filename}': {e}")


def create_target_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        print(f'No such directory: {directory_path}')
        print(f'Creating: {directory_path}')
        try:
            os.mkdir(directory_path)
        except OSError as e:
            print(f"Error creating directory '{directory_path}': {e}")
            exit(TO_PATH_CREATING_ERROR)


def check_source_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        print(f'No such directory: {directory_path}')
        exit(FROM_PATH_NOT_EXISTS)
    return True


def main():
    args = get_parser().parse_args()
    from_path = args.from_path
    to_path = args.to_path
    extension = args.extension

    if check_source_directory_exists(from_path):
        create_target_directory_if_not_exists(to_path)
        copy_files(from_path, to_path, extension)


if __name__ == '__main__':
    main()

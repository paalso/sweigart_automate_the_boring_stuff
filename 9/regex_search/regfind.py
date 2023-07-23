#!/usr/bin/env python3

# Searches for any line that matches a user-supplied regular expression in
# all files in a folder that matches a given file mask
# regfind -p './subdir*' -m '\d{2+}

import argparse
import colorama
import os
import re

DESCRIPTION = \
'''Searches for any line that matches a user-supplied regular expression in
all files in a folder that matches a given file mask'''

MASK_CHUNK_COLOR = colorama.Fore.RED
FILENAME_COLOR = colorama.Fore.GREEN
FILENAME_LINE_SEPARATOR = ':'
FILENAME_LINE_SEPARATOR_COLOR = colorama.Fore.MAGENTA


def get_args():
    parser = argparse.ArgumentParser(DESCRIPTION)

    parser.add_argument(
        'mask',
        help='regular expression mask to search in the specified files')

    parser.add_argument(
        '-p', '--path',
        default='.',
        help='path to the files to search, default is current directory')

    args = parser.parse_args()
    return args.mask, args.path


def print_line(file, line, regex):
    mask_chunks = regex.findall(line)
    split_text_chunks = regex.split(line)
    if mask_chunks:
        print(FILENAME_COLOR +
              f'{file}' +
              colorama.Style.RESET_ALL, end='')

        print(FILENAME_LINE_SEPARATOR_COLOR +
              FILENAME_LINE_SEPARATOR +
              colorama.Style.RESET_ALL, end='')

        print(split_text_chunks[0] +
              colorama.Style.RESET_ALL, end='')

        for text_chunk, matched_chunk in zip(split_text_chunks[1:],
                                             mask_chunks):
            print(MASK_CHUNK_COLOR +
                  matched_chunk +
                  colorama.Style.RESET_ALL, end='')
            print(text_chunk, end='')
        print(colorama.Style.RESET_ALL)


def print_file_matched_lines(file, regex):
    with open(file, 'r') as f:
        for line in f:
            print_line(file, line.rstrip(), regex)


def print_filename(filename):
    print(filename)


def main():
    mask, path = get_args()
    regex = re.compile(mask)

    colorama.init()

    for file in os.listdir(path):
        if os.path.isfile(file):
            print_file_matched_lines(file, regex)


if __name__ == '__main__':
    main()

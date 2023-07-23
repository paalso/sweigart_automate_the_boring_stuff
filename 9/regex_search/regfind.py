#!/usr/bin/env python3

# Searches for any line that matches a user-supplied regular expression in
# all files in a folder that matches a given file mask
# regfind -p './subdir*' -m '\d{2+}

import argparse
import colorama
import os
import re

PARSER_DESCRIPTION = \
'''Searches for any line that matches a user-supplied regular expression in
all files in a folder that matches a given file mask'''

MASK_CHUNK_COLOR = colorama.Fore.RED
FILENAME_COLOR = colorama.Fore.GREEN
FILENAME_LINE_SEPARATOR = ':'
FILENAME_LINE_SEPARATOR_COLOR = colorama.Fore.MAGENTA


def get_args():
    parser = argparse.ArgumentParser(PARSER_DESCRIPTION)

    parser.add_argument(
        'mask',
        help='regular expression mask to search in the specified files')

    parser.add_argument(
        '-p', '--path',
        default='.',
        help='path to the files to search, default is current directory')

    args = parser.parse_args()
    return args.mask, args.path


def print_line(line, regex, filename, first_find_flag):
    mask_chunks = regex.findall(line)
    split_text_chunks = regex.split(line)

    if first_find_flag:
        print_filename(filename)

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
    first_find_flag = True
    with open(file, 'r') as f:
        for line in f:
            if is_mask_in_line(line, regex):
                print_line(line.rstrip(), regex, file, first_find_flag)
                first_find_flag = False


def is_mask_in_line(line, regex):
    return regex.search(line)


def print_filename(filename):
    print(FILENAME_COLOR +
          f'{filename}' +
          colorama.Style.RESET_ALL, end='')

    print(FILENAME_LINE_SEPARATOR_COLOR +
          FILENAME_LINE_SEPARATOR +
          colorama.Style.RESET_ALL)


def main():
    mask, path = get_args()
    regex = re.compile(mask)

    colorama.init()

    for file in os.listdir(path):
        if os.path.isfile(file):
            print_file_matched_lines(file, regex)


if __name__ == '__main__':
    main()

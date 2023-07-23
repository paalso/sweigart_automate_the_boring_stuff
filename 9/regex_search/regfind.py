#!/usr/bin/env python3

# Searches for any line that matches a user-supplied regular expression in
# all files in a folder that matches a given file mask
# regfind -p './subdir*' '\d{2+}'

import argparse
import colorama
import glob
import re

PARSER_DESCRIPTION = \
'''Searches for any line that matches a user-supplied regular expression in
all files in a folder that matches a given file mask'''

REGEX_CHUNK_COLOR = colorama.Fore.RED
FILENAME_COLOR = colorama.Fore.GREEN
FILENAME_LINE_SEPARATOR = ':'
FILENAME_LINE_SEPARATOR_COLOR = colorama.Fore.MAGENTA


def get_args():
    parser = argparse.ArgumentParser(PARSER_DESCRIPTION)

    parser.add_argument(
        'regex',
        help='regular expression to search in the specified files')

    parser.add_argument(
        '-m', '--mask',
        default='*',
        help='path to the files to search, default is current directory')

    args = parser.parse_args()
    return args.regex, args.mask


def print_line(line, regex, filename, first_find_flag):
    regex_chunks = regex.findall(line)
    split_text_chunks = regex.split(line)

    if first_find_flag:
        print_filename(filename)

    print(split_text_chunks[0] +
          colorama.Style.RESET_ALL, end='')

    for text_chunk, matched_chunk in zip(split_text_chunks[1:],
                                         regex_chunks):
        print(REGEX_CHUNK_COLOR +
              matched_chunk +
              colorama.Style.RESET_ALL, end='')
        print(text_chunk, end='')
    print(colorama.Style.RESET_ALL)


def print_file_matched_lines(file, regex):
    first_find_flag = True
    with open(file, 'r') as f:
        for line in f:
            if is_regex_in_line(line, regex):
                print_line(line.rstrip(), regex, file, first_find_flag)
                first_find_flag = False


def is_regex_in_line(line, regex):
    return regex.search(line)


def print_filename(filename):
    print(FILENAME_COLOR +
          f'{filename}' +
          colorama.Style.RESET_ALL, end='')

    print(FILENAME_LINE_SEPARATOR_COLOR +
          FILENAME_LINE_SEPARATOR +
          colorama.Style.RESET_ALL)


def process(regex, file_mask):
    for path in sorted(glob.glob(file_mask)):
        print_file_matched_lines(path, regex)


def main():
    regex, file_mask = get_args()
    regex = re.compile(regex)

    colorama.init()
    process(regex, file_mask)


if __name__ == '__main__':
    main()

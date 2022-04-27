#!/usr/bin/env python3

import sys
import re

KEYWORDS = ['adjective', 'noun', 'verb']


def read_keywords(keywords):
    print('Input replacements for given keywods')
    return {keyword: input(f'Enter an {keyword}: ') for keyword in keywords}


def replace_keywords(filename, replacements, case_insensitive=True):
        def handle_line(line):
            for word in replacements:
                replacement = replacements[word]
                regex = re.compile(word, re.I) if case_insensitive \
                        else re.compile(word)
                return regex.sub(replacement, line)

        lines = open(filename,'r').readlines()
        open(filename,'w').writelines((map(handle_line, lines)))


def main():
    replaсements = read_keywords(KEYWORDS)
    replace_keywords(sys.argv[1], replaсements)


if __name__ == '__main__':
    main()

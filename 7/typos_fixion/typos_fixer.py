#!/usr/bin/env python3

# https://automatetheboringstuff.com/2e/chapter7/

# Find common typos such as multiple spaces between words, accidentally
# accidentally repeated words, or multiple exclamation marks at the end
# of sentences. Those are annoying!!


import sys
import re


fixes_to_make = {
    re.compile('([?!;,])+ '): r'\1 ',
    re.compile('([?!;,])+$'): r'\1',
    re.compile(r'(\b\w+\b)\s+\1'): r'\1',
    re.compile(' +'): ' ',
    re.compile(' +$'): '',
}


def parse_args():
    if len(sys.argv) != 2:
        print('Usage: {sys.argv[0]} filename')
        sys.exit(1)
    return sys.argv[1]


def generate_fixed_filename(filename, suffix):
    return f'{filename}-{suffix}'


def sub_typos(regexes, filename):
    fixed_filename = generate_fixed_filename(filename, 'FIXED')
    with open(filename, 'r') as f_in, open(fixed_filename, 'w') as f_out:
        for line in f_in:
            for regex, regex_fixer in fixes_to_make.items():
                line = regex.sub(regex_fixer, line)
            f_out.write(line)


def main():
    filename = parse_args()
    sub_typos(fixes_to_make, filename)


if __name__ == '__main__':
    main()

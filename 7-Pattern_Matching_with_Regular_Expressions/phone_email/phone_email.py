#!/usr/bin/env python3

# Finds phone numbers and email addresses on the clipboard
# находит телефонные адреса и адреса электронной почты в буфере обмена
# и выводит в буфер обмена и на печать в нормализованном виде -
# для телефонов 415-863-9900 | 415-863-9900 x123
# https://nostarch.com/contactus/

import re
import pyperclip
import sys

INPUT_ERR_MSG = '''Usage: {script_name} [filename]')
print('If no file is specified, then the text is got from the clipboard')'''

PHONES_REGEX = re.compile(r'''
    \b\(?(\d{3})\)?
    [-\.\s]?
    (\d{3})
    [-\.\s]?
    (\d{4})
    (\s?(x|ext)\.?\s?(\d{2,5}))?\b
''', re.VERBOSE)

EMAILS_REGEX = re.compile(r'''
    \b[\w\.\+-]+
    @
    (?:[\w\.\+-]+\.){1,2}
    [a-z]{2,4}\b
''', re.VERBOSE)


def gen_standart_phone(match):
    standart_phone = f'{match[0]}-{match[1]}-{match[2]}'
    if match[-1]:
        standart_phone = f'{standart_phone} x{match[-1]}'
    return standart_phone


def gen_standart_email(match):
    return match


PATTERNS = ((PHONES_REGEX, gen_standart_phone),
            (EMAILS_REGEX, gen_standart_email))


def find_matches(text, patterns):
    return [normalizer(match)
            for regex, normalizer in patterns
            for match in regex.findall(text)]


def parse_args():
    args = sys.argv
    if len(args) > 2:
        print(INPUT_ERR_MSG.format(args[0]))
        sys.exit(1)
    if len(args) == 2:
        return args[1]


def main():
    input_ = parse_args()
    if not input_:
        text = pyperclip.paste()
    else:
        try:
            with open(input_) as f:
                text = f.read()
        except IOError:
            print(f'Cannot read file {input_}')
            exit(2)
    result = find_matches(text, PATTERNS)
    print(*result, sep='\n'
          if result else 'No phone numbers or email addresses found.')


if __name__ == '__main__':
    main()

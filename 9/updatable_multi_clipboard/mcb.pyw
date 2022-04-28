#!/usr/bin/env python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import argparse
import pyperclip
import shelve


def print_n_copy(content):
    print(content)
    pyperclip.copy(str(content))


def get_args():
    parser = argparse.ArgumentParser(
        description = 'Saves and loads pieces of text to the clipboard.')
    parser.add_argument('keyword', nargs='?',
        help='keyword to save / load clipboard to / from')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--save', action="store_true",
        help='saves clipboard to the keyword')
    group.add_argument('-l', '--list', action='store_true',
        help='loads all keywords to clipboard')
    group.add_argument('-d', '--delete', default=False, action='store_true',
        help='delete the keyword from the shelf')
    group.add_argument('-c', '--clear', default=False, action='store_true',
        help='clears the shelf')
    return parser.parse_args()


def main():
    args = get_args()
    with shelve.open('mcb.dat') as mcb_shelf:
        if args.save:
            mcb_shelf[args.keyword] = pyperclip.paste()
        elif args.list:
            print_n_copy(list(mcb_shelf.keys()))
        elif args.delete:
            mcb_shelf.pop(args.keyword, None)
        elif args.clear:
            mcb_shelf.clear()
        else:
            if args.keyword in mcb_shelf:
                print_n_copy(mcb_shelf[args.keyword])
            else:
                print(f'Keyword \'{args.keyword}\' not found')
                pyperclip.copy('')


if __name__ == '__main__':
    main()

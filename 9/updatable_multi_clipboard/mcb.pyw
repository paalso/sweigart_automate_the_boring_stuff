#!/usr/bin/env python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import argparse
import pyperclip
import shelve


def get_args():
    parser = argparse.ArgumentParser(
        description='Update / get data from Multi Clipboard')
    parser.add_argument('keywords', nargs='+',
        help='keywords to save (--save == True) / load (--save == False)' +\
            ' clipboard to / from')
    parser.add_argument('-s', '--save', default=False, action="store_true",
        help='saves clipboard to keyword')
    return parser.parse_args()


def main():
    args = get_args()
    with shelve.open('mcb.dat') as mcb_shelf:
        if args.save:
            for key in args.keywords:
                mcb_shelf[key] = pyperclip.paste()
        else:
            pyperclip.copy('\n'.join(mcb_shelf[key] for key in args.keywords if key in mcb_shelf))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys
import re

KEYWORDS = ["adjective", "noun", "verb"]


def sub_keywords_in_line(line, keywords):
    regex = re.compile(
        r"{}".format("|".join(map(lambda e: f"\\b{e}\\b", keywords))), re.I
    )
    for e in regex.finditer(line):
        replacement = input(f"Enter an {e.group()}: ")
        line = regex.sub(replacement, line, count=1)
    return line


def main():
    filename = sys.argv[1]
    lines = open(filename, "r").readlines()
    open(filename, "w").writelines(
        map(lambda line: sub_keywords_in_line(line, KEYWORDS), lines)
    )


if __name__ == "__main__":
    main()

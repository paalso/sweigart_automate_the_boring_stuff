#!/usr/bin/env python3


import colorama
import re


def process_line(line, regex):
    colorama.init()
    mask_chunks = regex.findall(line)
    split_text_chunks = regex.split(line)
    print(split_text_chunks[0], end='')
    for text_chunk, matched_chunk in zip(split_text_chunks[1:], mask_chunks):
        print(colorama.Fore.GREEN + matched_chunk +
              colorama.Style.RESET_ALL, end='')
        print(text_chunk, end='')
    print(colorama.Style.RESET_ALL)


s = 'fd b123y sd c985casdc c988y dac'
s = '123y sd c985casdc c9848y dac999'
mask = r'\b[abc]\d{3}[xyz]\b'
mask = r'\d{3}'

regex = re.compile(mask)

print(s)
process_line(s, regex)
print('Final line')

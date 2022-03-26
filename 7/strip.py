#!/usr/bin/env python3


# Regex Version of the strip() Method
# ====================================

# Write a function that takes a string and does the same thing as
# the strip() string method. If no other arguments are passed other
# than the string to strip, then whitespace characters will be
# removed from the beginning and end of the string. Otherwise,
# the characters specified in the second argument to the function
# will be removed from the string.


import re


def strip(string, characters=None):
    if characters:
        while True:
            for c in characters:
                print(c)
                s_cleared = re.sub('^'+c+'+', '', string)
                s_cleared = re.sub(c+'+'+'$', '', s_cleared)
                print(s_cleared)
            print(string, s_cleared)
            if string == s_cleared:
                break
            string = s_cleared
            print()
    return string


text = 'qwwwwertywqwqqqwww'
print(text)
print(strip(text, 'qw'))

# text = 'qwwawwaertywqwqqaqwaww'
# s = text.strip('qaw')
# print(s)

# text = 'qwswawwaertywqwqqaqwaww'
# s = text.strip('qaw')
# print(s)

# assert strip(" asc ")

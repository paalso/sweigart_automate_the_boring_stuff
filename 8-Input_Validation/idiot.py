#!/usr/bin/env python3

# How to Keep an Idiot Busy for Hours
# =====================================

# Ask the user if they’d like to know how to keep an idiot busy for hours.
# If the user answers no, quit.
# If the user answers yes, go to Step 1.

import pyinputplus as pyip


while True:
    response = pyip.inputYesNo(
        "Want to know how to keep an idiot busy for hours?\n")
    if response == 'no':
        print('Thank you. Have a nice day.')
        break

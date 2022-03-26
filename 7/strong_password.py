#!/usr/bin/env python3


# Strong Password Detection
# ==========================

# Write a function that uses regular expressions to make sure the password
# string it is passed is strong. A strong password is defined as one that is
# at least eight characters long, contains both uppercase and lowercase
# characters, and has at least one digit. You may need to test the string
# against multiple regex patterns to validate its strength.

# 1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
# 2. Минимум 1 число от [0–9]
# 3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
# 4. Минимум 1 специальный символ
# 5. Минимальная длина пароля : 6
# 6. Максимальная длина пароля: 12

# https://automatetheboringstuff.com/2e/chapter7/


import re


def check_password(token):
    return 7 < len(token) < 13 and \
           re.search('\d', token) and \
           re.search('[a-z]', token) and \
           re.search('[A-Z]', token) and \
           re.search("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", token)


assert check_password(r'as*cL_JLK5')
assert check_password(r'as*cL_JLK5')
assert not check_password(r'aA5&')
assert not check_password(r'ascLJLK5')
assert not check_password(r'@[5AAAAAA')
assert not check_password(r'@[5aaaaaa')
assert not check_password(r'@[a555555')
assert not check_password(r'@[AAAAAaa')

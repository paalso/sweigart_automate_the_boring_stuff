#! python3
# Программа для хранения паролей

import pyperclip
import sys
import json


if len(sys.argv) < 2:
    print("Использование: python3 pw [имя учетной записи]")
    sys.exit()

account = sys.argv[1]
with open("data.json", "r") as read_file:
    data = json.load(read_file)
    try:
        pyperclip.copy(data[account])
        print("OK!")
    except KeyError:
        print('Учетная запись {} отсутствует в базе'.format(account))
        sys.exit()

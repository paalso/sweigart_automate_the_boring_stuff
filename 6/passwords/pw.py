#! python3
# Программа для хранения паролей

import pyperclip, json, time, sys

DB_NAME = "D:\paals\Dropbox\Павел\Приватное\data.json"
SLEEP_TIME = 1.5

_input = input("Your input: ").split()
if len(_input) not in (1, 2):
    print("Incorrect input")
    time.sleep(SLEEP_TIME)
    sys.exit()

try:
    with open(DB_NAME, "r") as read_file:
        data = json.load(read_file)
        if len(_input) == 1:
            account = _input[0]
            try:
                pyperclip.copy(data[account])
            except KeyError:
                print("No account '{}' in your database".format(account))
                time.sleep(SLEEP_TIME)
                sys.exit()
        else:
            account, password = _input
            data[account] = password
            with open(DB_NAME, "w") as write_file:
                json.dump(data, write_file)
        print("OK!")

except IOError:
    print("File '{}' not found".format(DB_NAME))

time.sleep(SLEEP_TIME)


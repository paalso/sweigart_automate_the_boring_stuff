#!/usr/bin/env python3

import random
import time

NUMBER_OF_QUESTIONS = 10
TIME_LIMIT = 8
TRIES_LIMIT = 3


def check_input(line, num1, num2):
    return f'{num1 * num2}' == line.strip()


correctAnswers = 0
for questionNumber in range(1, NUMBER_OF_QUESTIONS + 1):
    num1 = random.randrange(2, 9)
    num2 = random.randrange(2, 9)
    start_time = time.time()
    out_of_time = False
    for tries in range(TRIES_LIMIT):
        answer = input(f'#{questionNumber:<2}: {num1} x {num2} = ')
        is_correct_answer = check_input(answer, num1, num2)
        if not is_correct_answer:
            print('Incorrect!')
        if time.time() - start_time > TIME_LIMIT:
            out_of_time = True
            break
        if is_correct_answer:
            print('Correct!')
            correctAnswers += 1
            break
    if out_of_time:
        print('Out of time')
        continue
    if not is_correct_answer:
        print('Out of tries!')
    time.sleep(0.5)

print(f'Score: {correctAnswers} / {NUMBER_OF_QUESTIONS}')

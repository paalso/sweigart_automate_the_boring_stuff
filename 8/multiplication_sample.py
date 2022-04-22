#!/usr/bin/env python3

import pyinputplus as pyip
import random
import time

NUMBER_OF_QUESTIONS = 10
TIME_LIMIT = 8
TRIES_LIMIT = 3

correctAnswers = 0

for questionNumber in range(NUMBER_OF_QUESTIONS):
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    prompt = f'#{questionNumber}: {num1} x {num2} = '
    try:
    # Right answers are handled by allowRegexes.
    # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt,
                      allowRegexes=[f'^{num1 * num2}$'],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=TIME_LIMIT, limit=TRIES_LIMIT)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    
    time.sleep(1) # Brief pause to let user see the result.

print(f'Score: {correctAnswers} / {NUMBER_OF_QUESTIONS}')

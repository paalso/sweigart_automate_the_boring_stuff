#!/usr/bin/env python3

# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
import string
from capitals import CAPITALS

NUMBER_OF_QUIZES = 2
ANSWERS_NUMBER = 4

quiz_header = \
'''Name:

Date:

Period:

                    State Capitals Quiz (Form {})

'''


def generate_quiz_item(item_num: int,
                       state: str,
                       capitals: list,
                       answers_number=ANSWERS_NUMBER):
    answers_ids = string.ascii_uppercase[:answers_number]
    answers = [correct_answer := capitals[state]]
    possible_answers = list(capitals.values())
    possible_answers.remove(correct_answer)
    answers.extend(random.sample(possible_answers, answers_number - 1))
    random.shuffle(answers)

    correct_answer = answers_ids[answers.index(correct_answer)]
    quiz_item_options = (
        f'    {answers_ids[i]}. {answer}' for i, answer in enumerate(answers) 
    )
    quiz_text = f'{item_num}. What is the capital of {state}?\n' + \
                '\n'.join(quiz_item_options) + '\n'
    return (quiz_text, correct_answer)


def generate_quiz(num: int):
    quiz_content = [quiz_header.format(num)]
    answers = []
    states = list(CAPITALS.keys())
    random.shuffle(states)

    for i, state in enumerate(states):
        quiz_item, answer = generate_quiz_item(i + 1, state, CAPITALS)
        quiz_content.append(quiz_item)
        answers.append(f'{i + 1}. {answer}')

    return ('\n'.join(quiz_content), '\n'.join(answers))


def generate_quiz_files(num: int):
    quiz, answers = generate_quiz(num)
    with open(f'capitalsquiz{num}.txt', 'w') as f:
        f.write(quiz)
    with open(f'capitalsquiz_answers{num}.txt', 'w') as f:
        f.write(answers)


def main():
    for i in range(1, NUMBER_OF_QUIZES + 1):
        generate_quiz_files(i)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
CAPITALS = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

NUMBER_OF_QUIZES = 3

quiz_header = \
'''Name:

Date:

Period:

                    State Capitals Quiz (Form 1)


'''

def generate_quiz_item(item_num: int,
                       state: str,
                       capitals: list,
                       answers_num=4):
    answers = [correct_answer := capitals[state]]
    possible_answers = list(capitals.values())
    possible_answers.remove(correct_answer)
    random.shuffle(possible_answers)
    answers.extend(possible_answers[:answers_num - 1])
    random.shuffle(answers)

    correct_answer = chr(ord('A') + answers.index(correct_answer))
    quiz_item_options = (
        f'    {chr(ord("A") + i)}. {answer}' for i, answer in enumerate(answers) 
    )
    quiz_text = f'{item_num}. What is the capital of {state}?\n' + \
                '\n'.join(quiz_item_options) + '\n'
    return (quiz_text, correct_answer)


def generate_quiz():
    quiz = quiz_header
    answers = []
    states = list(CAPITALS.keys())
    random.shuffle(states)

    for i, state in enumerate(states):
        quiz_item, answer = generate_quiz_item(i + 1, state, CAPITALS)
        quiz += quiz_item
        answers.append(f'{i + 1}. {answer}')
    
    return (quiz, '\n'.join(answers))


def generate_quiz_files(num: int):
    quiz, answers = generate_quiz()
    with open(f'capitalsquiz{num}.txt', 'w') as f:
        f.write(quiz)
    with open(f'capitalsquiz_answers{num}.txt', 'w') as f:
        f.write(answers)


def main():
    for i in range(NUMBER_OF_QUIZES):
        generate_quiz_files(i + 1)


if __name__ == '__main__':
    main()

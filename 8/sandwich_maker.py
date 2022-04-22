#!/usr/bin/env python3

from random import choices
import pyinputplus as pyip

PRICES = {
    'wheat': 0.30,
    'white': 0.45,
    'sourdough': 0.65,
    'chicken': 0.85,
    'turkey': 1.20,
    'ham': 1.05,
    'tofu': 0.60,
    'cheddar': 0.65,
    'Swiss': 0.85,
    'mozzarella': 0.90,
    'mayo': 0.10,
    'mustard': 0.15,
    'lettuce': 0.20,
    'tomato': 0.15
}

choices = []

print('Tell us about your sandwich preferences')

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                            prompt='Which bread type woild you prefer?\n')
choices.append(bread_type)

protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                              prompt='Which protein type would you prefer?\n')
choices.append(protein_type)

want_cheese = pyip.inputYesNo('Do you want cheese?\n')
if want_cheese == 'yes':
    cheese_type = \
        pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
                       prompt='Which cheese type woild you prefer?\n')
    choices.append(cheese_type)

for sauce in 'mayo', 'mustard', 'lettuce', 'tomato':
    sauce_option = pyip.inputYesNo(f'Do you want {sauce}?\n')
    if sauce_option  == 'yes':
        choices.append(sauce)

sandwiches_number = pyip.inputInt('How many sandwiches do you want?\n',
                                min=1, max=5)

cost_per_sandwiche = sum(PRICES[product] for product in choices)
total_cost = cost_per_sandwiche * sandwiches_number
print(f'Your sandwiche price is {cost_per_sandwiche:.2f},', 
      f'total cost is {total_cost:.2f}')

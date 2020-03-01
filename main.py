'''
    second player is computer
'''

import random

user = str(input("Rock, Scissors or Paper? "))
computer = ['Rock', 'Scissors', 'Paper']

def expressions():


if user == 'Rock':
    print(random.choice(computer))

if user == 'Paper':
    print(random.choice(computer))

if user == 'Scissors':
    print(random.choice(computer))

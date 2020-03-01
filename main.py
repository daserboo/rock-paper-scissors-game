'''
    second player is computer
'''

import random

user = str(input("Rock, Scissors or Paper? \n"))
computer = ['Rock', 'Scissors', 'Paper']

x = random.choice(computer)

if user == 'Rock':
    if x == 'Paper':
        print(x, "\nYou lose!")
    elif x == 'Scissors':
        print(x, "\nYou win!")
    else:
        print(x, '\nStandoff')

if user == 'Paper':
    if x == 'Rock':
        print(x, "\nYou win!")
    elif x == 'Scissors':
        print(x, "\nYou lose!")
    else:
        print(x, '\nStandoff')

if user == 'Scissors':
    if x == 'Paper':

        print(x, "\nYou win!")
    elif x == 'Rock':
        print(x, "\nYou lose!")
    else:
        print(x, '\nStandoff')

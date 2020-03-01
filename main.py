'''
    second player is computer
'''

import random

user = str(input("Rock, Scissors or Paper? \n"))
computer = ['Rock', 'Scissors', 'Paper']

x = random.choice(computer)

while user != 'Rock' or user != 'Paper' or user != 'Scissors':
    user = str(input("Rock, Scissors or Paper? \n"))
    if user == 'Rock' or user == 'Paper' or user == 'Scissors':
        if user == computer:
            print('Tie!\n')
        if user == 'Rock':
            if x == 'Paper':
                print(x, '\nYou lose!\n')
            elif x == 'Scissors':
                print(x, '\nYou win!\n')
        if user == 'Paper':
            if x == 'Rock':
                print(x, '\nYou win!\n')
            elif x == 'Scissors':
                print(x, '\nYou lose!\n')
        if user == 'Scissors':
            if x == 'Paper':
                print(x, '\nYou win!\n')
            elif x == 'Rock':
                print(x, '\nYou lose!\n')

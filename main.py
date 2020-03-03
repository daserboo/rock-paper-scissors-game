'''
    second player is computer
'''

import random

def game():
    computer = ['Rock', 'Scissors', 'Paper']
    user = str(input("Rock, Scissors or Paper? \n"))
    x = random.choice(computer)

    if user == x:
        print(x, '\nTie!\n')

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

print(game())

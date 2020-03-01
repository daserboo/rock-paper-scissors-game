'''
    second player is computer
'''

import random

def game():
    computer = ['Rock', 'Scissors', 'Paper']
    user = None
    x = random.choice(computer)

    while user == None:
        user = str(input("Rock, Scissors or Paper? \n"))
        if user not in computer:
            print('repeat please \n', input())


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

print(game())

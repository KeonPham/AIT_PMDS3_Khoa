#Homework 1.2

import random

target_number = random.randint(1, 100)

def guessing_game():
    print('This is a guessing game where the system will generate a target number,\n'
          'and you will enter a guess until you meet the target. While inputting your '
          'guesses, there will be hints to guide you.')
    while True:
        guess_input = int(input('Please enter your guess here: '))
        if guess_input > target_number:
            print('Lesser than that')
        elif guess_input < target_number:
            print('Bigger than that')
        else:
            print('You are correct')
            break

guessing_game()
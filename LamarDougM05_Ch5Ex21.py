"""
A paper, rock, scissors game
Computer's choice is determined
by random number. User will choose and
then the choose's are compared.
Input validation for when a user continues
to enter the incorrect answer. 
"""

import random

#valid choices for user
VALID_CHOICES = ('ROCK','PAPER','SCISSORS')

#the game start
def start():
    num = random.randint(1, 3)
    if num == 1:
        computer = 'ROCK'
    elif num == 2:
        computer = 'PAPER'
    else:
        computer = 'SCISSORS'
    while True:
        user = input("Please choose rock, paper, or scissors: ")
        user = user.upper()
        if user in VALID_CHOICES : break

    return computer, user






def game(computer, user):
    while computer == user:
        print("Tie. Please choose again")
        computer, user = start()
    else:
        if computer == 'ROCK' and user == 'SCISSORS':
            print('Rock smashes scissors. Computer wins!')
        elif computer == 'SCISSORS' and user == 'ROCK':
            print('Rock smashes scissors. You win!')
        elif computer == 'PAPER' and user == 'SCISSORS':
            print('Scissors cut paper. You win!')
        elif computer == 'SCISSORS' and user == 'PAPER':
            print('Scissors cut paper. You win!')
        elif computer == 'ROCK' and user == 'PAPER':
            print('Paper covers rock. You win!')
        elif computer == 'PAPER' and user == 'ROCK':
            print('Paper covers rock. Computer wins!')

def main():
    computer, user = start()
    print(computer)
    game(computer, user)
    print("Doug Lamar")

main()


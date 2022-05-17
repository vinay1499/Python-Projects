#Rock-Paper-Scissors.

import random


def play():
    user_choice = input("What's your choice, 'r' for Rock, 'p' for paper, 's' scissors.")
    computer_choice = random.choice(['r','p','s'])

    if user_choice == computer_choice:
        return "It's a tie"
    elif user_won(user_choice, computer_choice):
        return "You Won!!"
    else:
        return "You Lost!!"

def user_won(player, opponent):
    if (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r'):
        return True

print(play())

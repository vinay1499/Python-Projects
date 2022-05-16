# Guess the number User.
# here we will make the computer to guess
import random
def computer_guess(x):
    low = 1
    high = x

    guess = random.randint(low,high)
    feedback = ''

    while feedback != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = high
        feedback=input(f"Computer's guess is {guess}. Enter the feedback, if it's high(h), if it's low(l), if it's correct(c)")
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"Yayy! The computer guessed the correct number {guess}.")

computer_guess(1000)

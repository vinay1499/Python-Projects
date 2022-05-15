#Guess the number (computer)

import random    #Generates random number.

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess=int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. It's too low.")
        elif guess>random_number:
            print("Sorry, guess again. It's too high.")
        
    print(f"Congrats, You have guessed the correct number {random_number}")

guess(10)

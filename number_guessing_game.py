# Number Guessing Game in Python

import random

lower_bound = 1
upper_bound = 100

answer = random.randint(lower_bound, upper_bound)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lower_bound} and {upper_bound}.")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {answer} in {guesses} tries.")
            is_running = False
    else:
        print("Invalid input.")
        print(f"Please enter a number between {lower_bound} and {upper_bound}.")

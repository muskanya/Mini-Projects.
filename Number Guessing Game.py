# Number Guessing Game

import random
def number_guessing_game():
    lowest = 1
    highest = 100
    secret_number = random.randint(lowest, highest)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    choice=input("Which mode do you want to play! Press c for challenge mode or n for normal mode: ").lower()

    if choice=="c":
        while True:
            guess = int(input(f"Guess a number between {lowest} and {highest}: "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again!")
            elif guess > secret_number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
                break

            if attempts == 10:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")
                break
    elif choice=="n":
        
        while True:
            guess = int(input(f"Guess a number between {lowest} and {highest}: "))

            if guess < secret_number:
                print("Too low. Try again!")
            elif guess > secret_number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the secret number")
                break

number_guessing_game()
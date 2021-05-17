#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from Day12_1_art import logo
import random


def subtract_tries():
    return tries_left - 1


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
answer = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# if loop to create tries_left
tries_left = 0
if difficulty == "easy":
    tries_left = 10
else:
    tries_left = 5

# make game_over flag
game_over = False
while tries_left > 0 and not game_over:
    # while loop until input==answer or tries_left == 0
    guess = int(input(f"You have {tries_left} attempts remaining to guess the number.\nMake a guess: "))
    # if loop to check answer vs input
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        game_over = True
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")

    # run subtract tries_left algo
    if not game_over:
        tries_left = subtract_tries()
        # if loop to check if tries_left == 0
        if tries_left == 0:
            print(f"You've run out of guesses, the answer was {answer}.")
            game_over = True
        else:
            print("Guess again.")

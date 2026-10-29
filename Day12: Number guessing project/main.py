import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_number, turns):
    if user_guess == actual_number:
        print(f"You got it! The answer was {actual_number}")
    elif user_guess > actual_number:
        print("Too high.")
        return turns -1
    elif user_guess < actual_number or turns >= 2:
        print("Too low.")
        return turns -1

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

print("Welcome to the Number Guessing Game!")
print(art.logo)
print("I'm thinking of a a number between 1 and 100.")
number = random.choice(range(1, 101))

turns = set_difficulty()

guess=0
while guess!=number:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, number, turns)
    if turns == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        game_over = True



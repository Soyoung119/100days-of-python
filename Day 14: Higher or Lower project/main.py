import art
from game_data import data
import random

def comparison(a_followers, b_followers, answer, score):
    if a_followers > b_followers and answer == "a":
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    elif a_followers < b_followers and answer == "b":
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    else:
        return score

# Generate a random account from the game data
def ran_number():
    return random.choice(data)

def generate():
    score = 0
    game_over = False
    b_number = 0

    while not game_over:
        # Display art
        print(art.logo)
        a_number = ran_number()
        # Format the account data in to printable format
        print(f"Compare A: {a_number['name']}, a {a_number['description']}, from {a_number['country']}")

        print(art.vs)
        b_number = ran_number()
        print(f"Against B: {b_number['name']}, a {b_number['description']}, from {b_number['country']}")

        # Ask user for a guess
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_count = a_number['follower_count']
        b_count = b_number['follower_count']
        score = comparison(a_count, b_count, answer, score)

        if a_count > b_count and answer == "b":
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
        elif a_count < b_count and answer == "a":
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

generate()







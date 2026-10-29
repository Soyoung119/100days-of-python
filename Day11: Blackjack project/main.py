import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit():
    shuffle = random.choice(cards)
    my_card.append(shuffle)

def calculator(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        score -= 10

    return score

play_card = True

while play_card:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    print(art.logo)
    my_card =[]
    for card in range(2):
        hit()
        print(my_card)
    print(f"Your cards: {my_card}, current score: {sum(my_card)}")

    dealer_card = []
    for card in range(2):
        shuffle = random.choice(cards)
        dealer_card.append(shuffle)
        print(dealer_card)
    print(f"Computer's first card: {dealer_card[0]}")

    new_sum = 0
    another_card = True
    while another_card:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_card == 'y':
            hit()
            score = calculator(my_card)
            print(f"Your cards: {my_card}, current score: {score}")
            print(f"Computer's first card: {dealer_card[0]}")
        else:
            another_card = False

    while sum(dealer_card) < 16:
        shuffle = random.choice(cards)
        dealer_card.append(shuffle)

    my_score = calculator(my_card)
    dealer_score = calculator(dealer_card)
    if my_score > 21 and 11 in my_card:
        print(f"Your final hand: {my_card}, final score: {my_score}")
    else:
        print(f"Your final hand: {my_card}, final score: {my_score}")
    print(f"Computer's final hand: {dealer_card}, final score: {dealer_score}")

    if my_score > 21:
        print("You went over. You lose")
    elif dealer_score > 21:
        print("Opponent went over. You win")
    elif my_score > 21 and dealer_score > 21:
        print("Both went over. Draw")
    elif my_score > dealer_score:
        print("Win with a Blackjack")
    elif my_score < dealer_score:
        print("You lose")

    if play_game == "n":
        play_card = False

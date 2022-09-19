""" Our Blackjack House Rules

The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""
import random

from art import logo




def blackjack():
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    players_cards = []
    computers_cards = []
    computer_score = 0

    while computer_score < 17:
        computers_cards.append(random.choice(cards))
        computer_score = sum(computers_cards)

    players_cards.append(random.choice(cards))

    another_card = True

    while another_card:
        players_cards.append(random.choice(cards))
        player_score = sum(players_cards)
        print(f"Your cards: {players_cards}, current score: {player_score}")
        print(f"Computer's first card: {computers_cards[0]}")
        if player_score < 21:
            move = input("Type 'y' to get another card, type 'n' to pass: ")
            if move == 'y':
                another_card = True
            else:
                another_card = False
        else:
            another_card = False

    print(f"Your final hand: {players_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")

    if player_score > 21 or (player_score < computer_score <= 21):
        print("You lose 😤")
    elif player_score == computer_score:
        print("Draw")
    else:
        print("You win 😃")

    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if new_game == 'y':
        blackjack()


new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if new_game == 'y':
    blackjack()
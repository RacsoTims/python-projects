"""
Author: O. Smit

Description:

Simulates a game wherein one must guess whether the next
card from the deck will be red (being either hearts or diamonds)
or black (being either clubs or spades).
"""

from sys import argv
import numpy as np
import random
from RB_deck import Deck


def score_frequencies(scores):
    array = np.array(scores)
    unique_scores, count_scores = np.unique(array, return_counts=True)
    return unique_scores, count_scores


a = int(argv[1])
b = int(argv[2])

count_red = a
count_black = a
times_simulated = b
score = 0
games = 0
total_score = 0

scores = []

my_deck = Deck()
if (a < 26):
    my_deck.switch(my_deck.deck_of_cards[0:a]
                   + my_deck.deck_of_cards[len(my_deck.deck_of_cards)
                                           // 2:(len(my_deck.deck_of_cards) // 2) + a])

while games < times_simulated:

    for i in range(0, len(my_deck.deck_of_cards)):
        first = my_deck.view(i)

        if count_red == count_black:
            r = random.randint(0, 1)
            if r == 0:
                guess = "red"
            elif r == 1:
                guess = "black"

        elif count_red > count_black:
            guess = "red"

        elif count_red < count_black:
            guess = "black"

        if first.get_suit() in ["hearts", "diamonds"]:
            first_colour = "red"
            count_red -= 1

        elif first.get_suit() in ["spades", "clubs"]:
            first_colour = "black"
            count_black -= 1

        if guess == first_colour:
            score += 1
        else:
            score = score

    scores.append(score)
    total_score += score
    score = 0
    games += 1
    my_deck = my_deck.shuffle()

unique_scores, count_scores = score_frequencies(scores)
print("Score of x/52:")
for j in range(0, len(unique_scores)):
    print(f"\t   {unique_scores[j]}", end='\t')
    print(f"{count_scores[j]} times", end='\t')
    print(f"   {round(float((count_scores[j] / games)) * 100, 2)}%")
print(f"Average score after {games} games: {total_score / games}")

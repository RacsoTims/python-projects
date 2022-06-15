"""
Author: O. Smit

Description:

Defines an ordinary deck of cards, consisting of
52 cards separated into four suits. You can call
various methods on the deck object.
"""


from RB_card import Card
import random


class Deck(object):

    def __init__(self):
        self.deck_of_cards = []

        suits = ["hearts", "diamonds", "spades", "clubs"]
        for kind in suits:
            for value in range(1, 14):
                self.deck_of_cards.append(Card(kind, value))

    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        return self

    def draw(self, index):
        return self.deck_of_cards.pop(index)

    def view(self, index):
        return self.deck_of_cards[index]

    def reset(self):
        return self.__init__()

    def switch(self, new_deck):
        self.deck_of_cards = new_deck
        return self

    def __str__(self):
        deck_of_cards = self.deck_of_cards
        return ' '.join(map(str, deck_of_cards))

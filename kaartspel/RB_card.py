"""
Author: O. Smit

Description:

Defines a playing card from an ordinary deck of cards. You
can call various methods on the card object.
"""


class Card(object):

    def __init__(self, suit, value, show=True):
        if suit in ["hearts", "diamonds", "spades", "clubs"]:
            self.suit = suit
            self.value = value
            self.show = show

        if self.suit == "hearts":
            self.suit_val = 127152
        elif self.suit == "diamonds":
            self.suit_val = 127168
        elif self.suit == "spades":
            self.suit_val = 127136
        elif self.suit == "clubs":
            self.suit_val = 127184
        else:
            raise Exception("Non-existent card.")

    def __str__(self):
        if self.show:
            return chr(self.suit_val + self.value)
        else:
            chr(127136)

    def get_suit(self):
        return str(self.suit)

    def get_value(self):
        return str(self.value)

    def closed_or_not_closed(self):
        if self.show is True:
            return not self.show
        if self.show is False:
            return not self.show

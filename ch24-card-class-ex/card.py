#!/usr/bin/env python3
"""
Chapter 24 - Deck of cards exercise
@author Ellery Penas
@version 2018.05.08
"""
from random import shuffle


class Card:
    allowed_suit = ["Hearts", "Clubs", "Diamonds", "Spades"]
    allowed_value = [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K"]

    def __init__(self, value, suit):
        if suit not in Card.allowed_suit or value not in Card.allowed_value:
            raise ValueError(f"Invalid suit/value combonation specifed")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):

        # using list comprehension
        self.cards = [
            Card(
                value,
                suit) for value in Card.allowed_value for suit in Card.allowed_suit]
        # using normal for loops
#        self.cards = []
#        for suit in Card.allowed_suit:
#            for value in Card.allowed_value:
#                self.cards.append(Card(value, suit))

    def __repr__(self):
        return f"There are {self.count()} cards left in the deck"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError("Cannot deal anymore cards. The deck is empty.")
        actual = min(count, num)
        dealt = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return dealt

    def deal_card(self):
        # will this clear the error?
        return self._deal(1)

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Can only shuffle a full deck!")
        shuffle(self.cards)


def main():
    """main line function"""
    d = Deck()
    print(d._deal(52))
    print(d)


if __name__ == "__main__":
    main()

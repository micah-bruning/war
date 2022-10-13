from card import Card
import random

"""
This class models a deck of cards. It initializes the 52 cards with the 4 suits.
"""
class Deck:

    def __init__(self):
        self.allCards = []

        suits = ["Diamond", "Heart", "Club", "Spade"]

        for s in suits:
            for num in range(1, 14):
                self.allCards.append(Card(value=num, suit=s))

    def getShuffledDeck(self):
        """
        This getter method returns a shuffled deck of cards using the
        'random' module

        :return: list of cards
        """
        random.shuffle(self.allCards)
        return self.allCards
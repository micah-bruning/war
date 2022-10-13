import unittest
from deck import Deck
from game import Game

class TestCardMethods(unittest.TestCase):

    def testDeckSizes(self):
        """
        This method tests that an exception is raised when a user tries to create a game
        where one or both players does not have a deck of 26 cards
        """
        with self.assertRaises(Exception):
            deck = Deck()
            shuffled_deck = deck.getShuffledDeck()

            g = Game(shuffled_deck[0:2], shuffled_deck[4:6])



if __name__ == '__main__':
    unittest.main()
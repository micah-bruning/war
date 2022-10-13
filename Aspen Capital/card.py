"""
This class models a card. Suit does not matter in the current
game of War, so not accessor method is implemented for suit.
"""
class Card:
    def __init__(self, value, suit):
        self.value = value

        if suit not in ["Spade", "Diamond", "Heart", "Club"]:
            raise ValueError("Invalid Suit")

        self.suit = suit


    def getValue(self):
        """
        Simple accessor for card's value

        :return: int
        """
        return self.value
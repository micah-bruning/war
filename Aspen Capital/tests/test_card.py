import unittest
from card import Card

class TestCardMethods(unittest.TestCase):

    def testInvalidSuit(self):
        """
        This method tests that an exception is raised for an invalid suit input
        """
        with self.assertRaises(ValueError):
            Card(1, "Spadez")

    def testCardValue(self):
        """
        This method tests that the cards value is correctly stored and accessed
        """
        c = Card(1, "Diamond")
        self.assertEqual(1, c.getValue())
        

if __name__ == '__main__':
    unittest.main()
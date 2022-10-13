import random

"""
This class models all of the logic of WAR. A Game object takes in two lists of cards. 
Its method playGame() returns the winner of each game.
"""
class Game:

    def __init__(self, playerOneCards, playerTwoCards):
        #Ensure proper card division for start of games
        if len(playerTwoCards) != 26 or len(playerOneCards) != 26:
            raise Exception("Game requires two lists of cards that are 26 in length")

        self.playerOneCards = playerOneCards
        self.playerTwoCards = playerTwoCards

    def playGame(self):
        """
        This method makes consecutive calls to playRounds() until an end game condition is met.
        It returns the winner of the game as a string

        :return: str
        """
        while self.isGameValid():
            roundWinner = self.playRound()

        if len(self.playerTwoCards) == 52 or len(self.playerOneCards) == 0:
            return "Player 2"

        if len(self.playerOneCards) == 52 or len(self.playerTwoCards) == 0:
            return "Player 1"

        return None

    def playRound(self):
        """
        This method models each round of War. Each player's top card is removed from their deck and is added
        to a list of 'winnings.' The player with the higher value card then has the winnings list of cards added
        to their own list with the collectCards() helper method. If the players cards tie in value, then they
        flip cards according to the tie-breaking condition outlined in the instructions. Those cards are also appended
        to the list of 'winnings.' Once a player flips a higher card, they then collect those winnings.

        returns: None
        """
        winnings = []

        p1Card = self.playerOneCards.pop(0)
        p2Card = self.playerTwoCards.pop(0)

        winnings.extend([p1Card, p2Card])

        #If one player's card is always added to the bottom first, then game can loop infintely, so switch up order
        random.shuffle(winnings)

        while p1Card.getValue() == p2Card.getValue():
            """
            While players are in 'WAR', only extract the face down and face up cards
            if player has cards left. If one player has no cards left while the recent card was a tie,
            then the player with any cards left wins.           
            """
            if not self.playerOneCards:
                return "Player 2"
            p1CardDown= self.playerOneCards.pop(0)

            if not self.playerTwoCards:
                return "Player 1"
            p2CardDown = self.playerTwoCards.pop(0)

            if not self.playerOneCards:
                return "Player 2"
            p1Card = self.playerOneCards.pop(0)

            if not self.playerTwoCards:
                return "Player 1"
            p2Card = self.playerTwoCards.pop(0)

            #Add new card to winnings, shuffle to prevent infinite games
            winnings.extend([p2CardDown, p1CardDown, p2Card, p1Card])
            random.shuffle(winnings)

        #If player one has a bigger card, collect the winnings
        if p1Card.getValue() > p2Card.getValue():
            self.playerOneCards = self.collectCards(winnings=winnings, playerCards=self.playerOneCards)
            return "Player 1"

        #If player two has a bigger card, collect the winnings
        else:
            self.playerTwoCards = self.collectCards(winnings=winnings, playerCards=self.playerTwoCards)
            return "Player 2"

    def collectCards(self, winnings, playerCards):
        """
        This method takes the cards that the winner of that round should receive and
        adds it to their deck.

        :param winnings: List of Cards
        :param playerCards: List of Cards of Player who won
        :return: playerCards with winning cards appended
        """
        for card in winnings:
            playerCards.append(card)

        return playerCards

    def isGameValid(self):
        """
        This method checks that neither player has zero or all of the cards, indicating the game
        can continue

        :return: bool
        """
        return len(self.playerTwoCards) != 0 and len(self.playerOneCards) != 0 and len(self.playerTwoCards) != 52 and len(self.playerOneCards) != 52





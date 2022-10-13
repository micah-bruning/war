import mysql.connector
from flask import Flask, render_template, jsonify
from game import Game
from deck import Deck

app = Flask(__name__)

@app.route('/')
def dbInit():
    '''
    This function initializes the scoring database. It first drops any existing database
    if it exists. Then, it creates the 'score' database and inserts player's 1 and 2 in with a score
    of zero. This endpoint can then be used to reset the total scores.

    returns: str (html template)
    '''
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS war")
    cursor.execute("CREATE DATABASE war")
    cursor.close()

    #Establish new connection to specific war db
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="war"
    )
    cursor = mydb.cursor()

    #Create wins Table
    cursor.execute('''CREATE TABLE wins 
                        (player_name VARCHAR(255), 
                        score INT, 
                        PRIMARY KEY(player_name))''')

    #Insert players one and two with a score of 0
    cursor.execute("INSERT INTO war.wins (player_name, score) values(%s, %s)", ("Player 1", 0))
    cursor.execute("INSERT INTO war.wins (player_name, score) values(%s, %s)", ("Player 2", 0))

    #Commit changes
    mydb.commit()
    cursor.close()

    return render_template("index.html")

@app.route('/start-game')
def startGame():
    """
    This endpoint starts a new game by creating a new instance of Game().
    The endpoint returns an html view with the winner displayed

    returns: str (html template)
    """
    #Create a deck and shuffle it
    deck = Deck()
    shuffled_deck = deck.getShuffledDeck()

    #Split the deck in half for each player
    playerOneCards = shuffled_deck[0:26]
    playerTwoCards = shuffled_deck[26:]

    #Start game and get its winner
    new_game = Game(playerOneCards, playerTwoCards)
    winner = new_game.playGame()

    #Connect to db and update score based on winner
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="war"
    )
    cursor = mydb.cursor()

    if winner == "Player 1":
        cursor.execute("UPDATE war.wins SET score = score + 1 WHERE player_name = 'Player 1'")
    else:
        cursor.execute("UPDATE war.wins SET score = score + 1 WHERE player_name = 'Player 2'")

    mydb.commit()
    cursor.close()

    return render_template("game-result.html", winner=winner)


@app.route('/lifetime-wins')
def getLifeTimeWins():
    """
    This method queries the 'score' table to get the total lifetime wins of Players One and Two.
    It then displays the score in an html view
    
    returns: str (html template)
    """
    #Connect to db
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="war"
    )
    cursor = mydb.cursor()

    #Select all from table and store in res
    cursor.execute("SELECT * FROM wins LIMIT 2")
    res = cursor.fetchall()
    cursor.close()

    return render_template("wins.html", res=res)

@app.errorhandler(404)
def page_not_found(e):
    """
    This method handles all requests to non-existent endpoints

    :param e: error
    :return: str (html template)
    """
    return render_template('error404.html'), 404

### Start App ###
if __name__ == "__main__":
  app.run(host ='0.0.0.0')

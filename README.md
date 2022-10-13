# Overview

I implemented WAR using Python's Flask framework. For the database, I used a mysql db in a docker container. 

# Running the Application

After cloning the repo into a local machine, open a terminal or cmd at Aspen Capital/ and run <code>docker compose up</code>. This will run the docker image as a container. 
  
  Head to localhost:8000 on your machine to view the home-page of the application. Alternatively, send a GET request to 
  the end-points listed below using the <code>curl localhost:8000/<endpoint></code> command in a terminal. The application returns
  basic html templates, so it is strongly advised to access it through a web-browser.
  
  # Application Endpoints
  
  1. '/' -- Home page of the application. (Re) Initializes the database
  
  2. '/start-game' -- Starts a new game of war and displays the winner of that game.
  
  3. '/lifetime-wins' -- Displays the lifetime wins stored in the MySQL database
  
  # Basic Game Design
  
  The game of war was built using three objects: Card, Deck and Game. The Card object models a card with a suit and a value property. The Deck contains fifty two cards with the standard suits and values. The Game object contains all of the logic for the game, and is responsible for the actual execution of the game. The Game object takes in two separate decks, one for each player. Class and method-level comments contain more in-depth details of the specific implementations. 
  
  # Game Design Limitations 
  There are a couple of key limitations to my game design: 
  
  First, to keep a consistent design, it might be helpful to create a 'Player' object that would keep track of its own cards instead of having a list of cards represent the player itself. Because the logic was fairly simple for this game, I kept my implementation as-is. If I wanted to expand the functionalities of the game, it would make sense to factor more logic out to a Player class.
  
  Second, it's possible for the game to terminate without one player collecting 52 cards, even though the adequate end-game condition is met and the proper winner is displayed. For example, suppose player one has 2 cards and player two has 50 cards at the start of a round. If the players flip their cards and receive a match, then player two will instantly win because player one does not have 3 total cards to gamble in that round. Within the logic of the game, player 2 never picks up those cards, but they are correctly designated as the winner. I wasn't entirely sure if this meant the second player would automatically win, but the rules online didn't specify so I made this assumption. 

  
 # App Design Limitations and Further Considerations
  Because of time constraints, I was only able to write a few basic unit tests for the game's functionalities. If I spent more time on the project, I would
  have restrucutred my Flask app to follow a Factory Pattern design and conducted tests on the app's different endpoints. Moreover, I would have liked to implement a UI that showcased the progress of each player at each round. Within the game class, the return value of each round is never used, but it could be if I were to create this UI.
  
  
  


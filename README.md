# Overview

I implemented WAR using Python's Flask framework. For the database, I used a mysql db in a docker container. 

# Running the Application

After cloning repo into local machine, run <code>docker compose up</code>
  at the root directory. This will run the docker image as a container. 
  
  Head to localhost:8000 on your machine to view the home-page of the application. Alternatively, send a GET request to 
  the end-points listed below using the <code>curl localhost:8000/<endpoint></code> command in a terminal. The application returns
  basic html templates, so it is strongly advised to access it through a web-browser.
  
  # Application Endpoints
  
  1. '/' -- Home page of the application. (Re) Initializes the database
  
  2. '/start-game' -- Starts a new game of war and displays the winner of that game.
  
  3. '/lifetime-wins' -- Displays the lifetime wins stored in the MySQL database
  
  # Game Design
  
  


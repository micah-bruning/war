# Running the Application

After cloning repo into local machine, run 

<code> docker compose up <code> 

at the root directory
  
In a local browser, head to localhost:8000 to view the index page of the app. Alternatively, use the <code>curl<code> 
command to set GET requests to the end-points listed in the next section. 
  
# Basic Structure
  
  The application is a simple Flask app that exposes three main endpoints:
  
    1. '/' -- Home page that (Re) Initializes Database 
  
    2. '/start-game' -- This starts a new game of war and returns an html view displaying which player one
  
    3. 


# Further Improvements

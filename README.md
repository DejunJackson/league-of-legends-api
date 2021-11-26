# league-of-legends-api

**This API is deployed on RapidAPI**. Visit [here](https://rapidapi.com/DejunJackson/api/league-of-legends-stats). 

# Description
One of my favorite games that I have been playing for years is [League of Legends](https://www.leagueoflegends.com/en-us/).
I decided I wanted to make some projects for this game, but I didn't see a lot of APIs available.
So, I created a web scraper that scraped all of the data for characters (or champions) in the game using the python module [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
I then cleaned the data, and created API endpoints using [FastAPI](https://fastapi.tiangolo.com/).

# Technologies used
1. **Python**
2. I used **FastAPI** for the endpoints.
3. **Beautiful Soup** to scrape the website that I needed and get the data.
4. **Pytest** for testing endpoints

# Run server locally
- Download the repo
- cd to the repo directory
- ```$ pip install "fastapi[all]"```
- ```$ pip install beautifulsoup4```
- Start the server - ```$ uvicorn main:app --reload``` 
- Make any requests using the endpoints below

# Testing
For testing each endpoint, I used the [pytest](https://docs.pytest.org/en/6.2.x/contents.html) testing module for python.

## Setup
- cd to the repo directory
- ```$ pip install -U pytest```
- Check to make sure it is installed - ```$ pytest --version```
- To run tests - ```$ py.test```
- Testing code is found in the test_cases directory


# API reference table

| Method    | Endpoint     | Description |  
| ----------- | ----------- | ----------|
| GET    | /champions      | Returns the name of every champion in the game |
| GET   | /champions/stats       | Returns a json object with all the base stats for every champion in the game |
| GET  | /champions/{name}/stats        | Returns json object of specified champion. (This is not case sensitive) |

# To-Do
- Scrape item data and add item endpoints
- Deploy API (DONE)
- Write tests (DONE)


### *Note*: *Instead of pip install individual dependencies, you could run* ```pip install -r requirements.txt``` *and skip the installing steps below*

import requests
import json


response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions/ekko/stats')
re = response.json()
print(type(re))
import requests
import json
from test_cases.secrets import API_KEY

url = "https://league-of-legends-stats.p.rapidapi.com/champions"

# Replace API_KEY with your rapidAPI key
headers = {
    'x-rapidapi-host': "league-of-legends-stats.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

response = requests.get(url, headers=headers)
re = json.loads(response.text)
print(re['champ_names'][0])
import requests
import json
from .secrets import API_KEY

url = "https://league-of-legends-stats.p.rapidapi.com/champions/stats"

# Replace API_KEY with your rapidAPI key
headers = {
    'x-rapidapi-host': "league-of-legends-stats.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

response = requests.get(url, headers=headers)

def test_get_champ_stats_check_status_code_equals_200():
    assert response.status_code == 200

def test_get_champ_stats_check_content_header_equals_json():
    assert response.headers["Content-Type"] == "application/json"

def test_get_champ_stats_check_first_name_equals_Aatrox():
    stats_list = json.loads(response.text)
    assert stats_list[0]["name"] == "Aatrox"
    
def test_get_champ_stats_check_length_is_158():
    stats_list = json.loads(response.text)
    assert len(stats_list) == 158






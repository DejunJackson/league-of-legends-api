import requests
import json
from .secrets import API_KEY

url = "https://league-of-legends-stats.p.rapidapi.com/champions"

# Replace API_KEY with your rapidAPI key
headers = {
    'x-rapidapi-host': "league-of-legends-stats.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

response = requests.get(url, headers=headers)



def test_get_champ_names_check_status_code_equals_200():
    assert response.status_code == 200

def test_get_champ_names_check_content_header_equals_json():
    assert response.headers["Content-Type"] == "application/json"

def test_get_champ_names_check_first_name_equals_Aatrox():
    res_text = json.loads(response.text)
    assert res_text["champ_names"][0] == "Aatrox"
    
def test_get_champ_names_check_length_is_159():
    res_text = json.loads(response.text)
    assert len(res_text["champ_names"]) == 159
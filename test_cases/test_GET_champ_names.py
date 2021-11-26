import requests
import json

def test_get_champ_names_check_status_code_equals_200():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions')
    assert response.status_code == 200

def test_get_champ_names_check_content_header_equals_json():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions')
    assert response.headers["Content-Type"] == "application/json"

def test_get_champ_names_check_first_name_equals_Aatrox():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions')
    response_body = response.json()
    champ_list = json.loads(response_body)
    assert champ_list["champ_names"][0] == "Aatrox"
    
def test_get_champ_names_check_length_is_159():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions')
    response_body = response.json()
    champ_list = json.loads(response_body)
    assert len(champ_list["champ_names"]) == 159
import requests
import json

def test_get_specific_champ_stats_check_status_code_equals_200():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions/ekko/stats')
    assert response.status_code == 200

def test_get_specific_champ_stats_check_content_header_equals_json():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions/ekko/stats')
    assert response.headers["Content-Type"] == "application/json"

def test_get_specific_champ_stats_check_name_equals_Ekko():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions/ekko/stats')
    response_body = response.json()
    stats_list = json.loads(response_body)
    assert stats_list['name'] == "Ekko"
    
def test_get_specific_champ_names_check_length_is_159():
    response = requests.get('https://league-of-legends-api-server.herokuapp.com/champions/ekko/stats')
    response_body = response.json()
    stats_list = json.loads(response_body)
    assert len(stats_list) == 19
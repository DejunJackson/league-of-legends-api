import requests
import json

def test_get_champ_stats_check_status_code_equals_200():
    response = requests.get('http://localhost:8000/champions/stats')
    assert response.status_code == 200

def test_get_champ_stats_check_content_header_equals_json():
    response = requests.get('http://localhost:8000/champions/stats')
    assert response.headers["Content-Type"] == "application/json"

def test_get_champ_stats_check_first_name_equals_Aatrox():
    response = requests.get('http://localhost:8000/champions/stats')
    response_body = response.json()
    stats_list = json.loads(response_body)
    assert stats_list[0]["name"] == "Aatrox"
    
def test_get_champ_stats_check_length_is_158():
    response = requests.get('http://localhost:8000/champions/stats')
    response_body = response.json()
    stats_list = json.loads(response_body)
    assert len(stats_list) == 158
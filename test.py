
import requests

res = requests.get('http://ddragon.leagueoflegends.com/cdn/11.23.1/data/en_US/champion.json')

print(res.text)
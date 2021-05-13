import requests
import json
url = "https://api-nba-v1.p.rapidapi.com/statistics/players/playerId/124"

headers = {
    'x-rapidapi-key': "a19b7cb12cmsh6930de9472375f5p1966d7jsn05abb0963e4e",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
print(response.text)
data = json.loads(response.text)
#print(json.dumps(data, indent=2))

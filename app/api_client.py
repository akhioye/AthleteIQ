import requests
import os 
import json

API_KEY = os.getenv("FOOTBALL_API_KEY")

def get_player_data(player_name):
    url = f"https://v3.football.api-sports.io/players?search={player_name}&season=2023"
    headers = {
        "x-apisports-key": "0675e46ccc9a2d82a91c49a933e4d6da"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("API Response: ")
        print(data)
        return data  # We’ll extract specific info later
    else:
        print(f"API error: {response.status_code}")
        return None
    

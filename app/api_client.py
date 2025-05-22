import requests
import os 
import json

API_KEY = os.getenv("FOOTBALL_API_KEY")

def get_id(player_name):

    if '%20' in player_name:
        first_name = player_name.split('%20')[0]
        last_name = player_name.split('%20')[-1]
    else:
        last_name = player_name

    url = f"https://v3.football.api-sports.io/players/profiles?search={last_name}"
    headers = {
        "x-apisports-key": "0675e46ccc9a2d82a91c49a933e4d6da"
        # "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data is None:
            return None
        else :
            return data  # We’ll extract specific info later
    
    else:
        print(f"API error: {response.status_code}")
        return None

def get_player_data(player_name):

    
    

    # Get player ID, league ID, and team ID
    dataprevious = get_id(player_name)

    if dataprevious is None:
        return None
    
    player_id = dataprevious['response'][0]['player']['id']
    


    url = f"https://v3.football.api-sports.io/players?id={player_id}&season=2023"
    headers = {
        "x-apisports-key": "0675e46ccc9a2d82a91c49a933e4d6da"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        if data is None:
            print("No data found for the player.")
            return None
        else :
            print("API Response: ")
            print(data)
            return data  # We’ll extract specific info later
    
    else:
        print(f"API error: {response.status_code}")
        return None
    

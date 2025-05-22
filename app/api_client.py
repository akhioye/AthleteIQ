import requests
import os 
import json
from urllib.parse import quote_plus as qoute_plus

API_KEY = os.getenv("FOOTBALL_API_KEY")


""" the get id function is not used in the current code, but it can be used to get the player id from the player name
    I decieded to just use the player name and league id but if you want to change it to only player name we have to use the id function
    then have another function to get the league id from the player id then add it to the the get palyer data function"""

# def get_id(player_name):

#     if '%20' in player_name:
#         first_name = player_name.split('%20')[0]
#         last_name = player_name.split('%20')[-1]
#     else:
#         last_name = player_name

#     url = f"https://v3.football.api-sports.io/players/profiles?search={last_name}"
#     headers = {
#         "x-apisports-key": "0675e46ccc9a2d82a91c49a933e4d6da"
#         # "x-apisports-key": API_KEY
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         if data is None:
#             return None
#         else :
#             return data  # We’ll extract specific info later
    
#     else:
#         print(f"API error: {response.status_code}")
#         return None

def get_player_data(player_name,league_id):
    

    season = 2023
    
    #handle spaces in name
    if ' ' in player_name:
        first_name = player_name.split(' ')[0]
        last_name = player_name.split(' ')[-1]
    else:
        last_name = player_name

    #handle special characters in name
    encoded_name = qoute_plus(last_name.strip())

    url = f"https://v3.football.api-sports.io/players?search={encoded_name}&league={league_id}&season={season}"
    headers = {
        "x-apisports-key": "0675e46ccc9a2d82a91c49a933e4d6da"
    }

    response = requests.get(url, headers=headers)
    print(f"API URL: {url}")
    if response.status_code == 200:
        data = response.json()

        if data is None:
            print("No data found for the player.")
            return None
        else :
            print("API Response: ")
            print(data)

            # I still need to handle special characters in the name
            # Check if there is more than one player
            
            # if data.get('response') and len(data['response']) > 0:
            #    for player in data['response']:
            #         if player['player']['firstname'].strip().lower() == first_name.strip().lower() and player['player']['lastname'].strip().lower() == last_name.strip().lower():
            #             # If the player is found, return the player data
            #             print("Player found: ")
            #             print(player)
            #             return player

            return data  # We’ll extract specific info later
    
    else:
        print(f"API error: {response.status_code}")
        return None
    

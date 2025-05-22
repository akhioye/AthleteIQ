from flask import render_template, request
from app import app
from app.api_client import get_player_data
from urllib.parse import quote_plus


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/player")
def player():
    name = request.args.get("name")
    league = request.args.get("league")
    if not name:
        return "Player name is required", 400
    if not league:
        return "League is required", 400

    # handle special characters in the player name
    player_name = name.strip()

    # Map league names to their respective IDs
    if league == "Premier League":
        league_id = 39
    elif league == "La Liga":  
        league_id = 140
    elif league == "Serie A":
        league_id = 135
    elif league == "Bundesliga":
        league_id = 78
    elif league == "Ligue 1":
        league_id = 61
   
    
    player_data = get_player_data(player_name, league_id)


    
    return render_template("player.html", player_name=name)

    

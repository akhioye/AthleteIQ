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
    LEAGUE_IDS = {
        "Premier League" : 39,
        "La Liga" : 140,
        "Serie A" : 135,
        "Bundesliga" : 78,
        "Ligue 1" : 61,
        "Eredivisie" : 88,
        "MLS" : 19,
        "UEFA Champions League" : 2,
        "UEFA Europa League" : 3,
        "Saudi Pro League" : 307
    }

    league_id = LEAGUE_IDS.get(league)
    if not league_id:
        return "Invalid league", 400
   
    
    player_data = get_player_data(player_name, league_id)


    
    return render_template("player.html", player_name=name,player_data=player_data)

    

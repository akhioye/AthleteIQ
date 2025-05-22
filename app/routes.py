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
    if not name:
        return "Player name is required", 400

    # handle special characters in the player name
    player_name = quote_plus(name)

    # Map league names to their respective IDs
   
    
    player_data = get_player_data(player_name)


    
    return render_template("player.html", player_name=name)

    

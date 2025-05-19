from flask import render_template, request
from app import app
from app.api_client import get_player_data


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/player")
def player():
    name = request.args.get("name")
    player_data = get_player_data(name)

    
    return render_template("player.html", player_name=name)

    

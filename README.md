# AthleteIQ

AthleteIQ is a Flask-based web app where users can search for a professional soccer player to view their season stats and relevant news. The goal is to provide an at-a-glance insight into both performance and public perception — powered by real APIs and sentiment analysis.

---

## ✅ Features

- Search for any professional soccer player
- View real-time season stats (goals, assists, appearances)
- (Coming soon) Recent news headlines + sentiment scoring
- (Coming soon) Player comparison view
- (Coming soon) Visual charts for performance trends

---

- **Backend:** Python, Flask
- **APIs:** API-Football (player data), NewsAPI (news – planned)
- **Frontend:** HTML, Jinja2 templates, CSS (Bootstrap optional)
- **Extras:** VADER or TextBlob (for sentiment analysis)

---

## 📁 Project Structure
AthleteIQ/
├── app/
│   ├── __init__.py          # Creates Flask app instance
│   ├── routes.py            # Defines routes like "/", "/player"
│   ├── api_client.py        # API-Football request logic
│   ├── sentiment.py         # (To be implemented) sentiment analysis for news
│   ├── templates/
│   │   ├── index.html       # Search form page
│   │   └── player.html      # Results page (shows player info)
│   └── static/
│       └── styles.css       # (Optional) styling for HTML
├── run.py                   # Entry point to run Flask app
├── requirements.txt         # Installed packages (Flask, requests etc.) 
├── README.md                # Project overview, setup, features
└── .gitignore               # Ignore virtual env, .env, cache files

Next step for now:
Take the API response from get_player_data(name) and: in routes.py

Pull out relevant fields (e.g. name, age, nationality, appearances, goals, etc.)

Pass those fields to the player.html template

Show them in a clean layout (can be just text or table for now)


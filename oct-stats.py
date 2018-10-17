import json
import requests

last_season = "https://api.sportradar.us/nba/trial/v5/en/games/2017/reg/schedule.json?api_key=dek9px59ega4h4vv3hjuw59p"
schedule_2017 = requests.get(last_season)
games_2017 = schedule_2017.json().get("games")

magic_id = "583ed157-fb46-11e1-82cb-f4ce4684ea4c"
pistons_id = "583ec928-fb46-11e1-82cb-f4ce4684ea4c"

heat_id = "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"
spurs_id = "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"

kings_id ="583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"
raptors_id = "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"

lakers_id = "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
timberwolves_id = "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"


def roster_url(team):
    head = "https://api.sportradar.us/nba/trial/v5/en/teams/"
    tail = "/profile.json?api_key=dek9px59ega4h4vv3hjuw59p"
    url = head + team + tail
    return url


def game_summary_url(game_id):
    head = "https://api.sportradar.us/nba/trial/v5/en/games/"
    tail = " /summary.json?api_key=dek9px59ega4h4vv3hjuw59p"
    url = head + game_id + tail
    return url


def oct_games(team, games_2017 = games_2017):
    games = []
    for g in games_2017:
        game_id = g.get("id")
        date = g.get("scheduled")
        oct_date = date.split("T")[0]
        d = oct_date[:-3]
        home = g.get("home")
        away = g.get("away")
        home_team = home.get("id")
        away_team = away.get("id")

        if d == "2017-10" and away_team == team:
            games.append(game_id)
        if d == "2017-10" and home_team == team:
            games.append(game_id)
    return games


lakers_games = oct_games(lakers_id)
timberwolves_games = oct_games(timberwolves_id)
magic_games = oct_games(magic_id,games_2017)
pistons_games = oct_games(pistons_id)
heat_games = oct_games(heat_id)
spurs_games = oct_games(spurs_id)
kings_games = oct_games(kings_id)
raptors_games = oct_games(raptors_id)



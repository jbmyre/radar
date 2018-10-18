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


def game_summary_url(game_id):
    head = "https://api.sportradar.us/nba/trial/v5/en/games/"
    tail = " /summary.json?api_key=dek9px59ega4h4vv3hjuw59p"
    url = head + game_id + tail
    return url


def oct_games(team, games_oct = games_2017):
    games = []
    for g in games_oct:
        game_id = g.get("id")  # type: string
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
magic_games = oct_games(magic_id)
pistons_games = oct_games(pistons_id)
heat_games = oct_games(heat_id)
spurs_games = oct_games(spurs_id)
kings_games = oct_games(kings_id)
raptors_games = oct_games(raptors_id)

lakers_game_ct = lakers_games.__len__()
timberwolves_game_ct = timberwolves_games.__len__()
magic_game_ct = magic_games.__len__()
pistons_game_ct = pistons_games.__len__()
heat_game_ct= heat_games.__len__()
spurs_game_ct = spurs_games.__len__()
kings_game_ct = kings_games.__len__()
raptors_game_ct = raptors_games.__len__()


def game_stats(games, team_id ):
    roster = []
    for g in games:
        game = requests.get(game_summary_url(g))
        home = game.json().get("home")
        away = game.json().get("away")
        home_id = home.get("id")
        away_id = away.get("id")
        if home_id == team_id:
            players = home.get("players")
        if away_id == team_id:
            players = away.get("players")
        roster.append(players)
    return roster

game_stats(lakers_games, lakers_id)

#cool

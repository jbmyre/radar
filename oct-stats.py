import json
import requests
from object import session
import model

last_season = "https://api.sportradar.us/nba/trial/v5/en/games/2017/reg/schedule.json?api_key=dek9px59ega4h4vv3hjuw59p"
schedule_2017 = requests.get(last_season)
games_2017 = schedule_2017.json().get("games")

magic_id = "583ed157-fb46-11e1-82cb-f4ce4684ea4c"
pistons_id = "583ec928-fb46-11e1-82cb-f4ce4684ea4c"
heat_id = "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"  # type: str
spurs_id = "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"
kings_id = "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"
raptors_id = "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"
lakers_id = "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
timberwolves_id = "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"


def game_summary_url(game_id):
    head = "https://api.sportradar.us/nba/trial/v5/en/games/"
    tail = " /summary.json?api_key=dek9px59ega4h4vv3hjuw59p"
    url = head + game_id + tail
    return url


def oct_games(team, games_oct=games_2017):
    games = []
    for g in games_oct:
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
magic_games = oct_games(magic_id)
pistons_games = oct_games(pistons_id)
heat_games = oct_games(heat_id)
spurs_games = oct_games(spurs_id)
kings_games = oct_games(kings_id)
raptors_games = oct_games(raptors_id)


def game_stats(games, team_id):
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


lakers_stats = game_stats(lakers_games, lakers_id)
timberwolves_stats = game_stats(timberwolves_games, timberwolves_id)
magic_stats = game_stats(magic_games, magic_id)
pistons_stats = game_stats(pistons_games, pistons_id)
heat_stats = game_stats(heat_games, heat_id)
spurs_stats = game_stats(spurs_games, spurs_id)
kings_stats = game_stats(kings_games, kings_id)
raptors_stats = game_stats(raptors_games, raptors_id)


def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value


def write_player_stats(stats, team_id):
    for p in stats:
        stat = nested_get(p, ["statistics"])
        player = model.Player()
        player.player_id = p.get("id")
        player.team_id = team_id
        player.first_name = p.get("first_name")
        player.last_name = p.get("last_name")
        player.jersey_number = p.get("jersey_number")
        player.points = stat.get("points")
        player.rebounds = stat.get("rebounds")
        player.assists = stat.get("assists")
        player.fg_percent = stat.get("field_goals_pct")
        session.add(player)
        session.flush()
        session.commit()


for stat in lakers_stats:
    write_player_stats(stat, lakers_id)

for stat in timberwolves_stats:
    write_player_stats(stat, timberwolves_id)

for stat in magic_stats:
    write_player_stats(stat, magic_id)

for stat in pistons_stats:
    write_player_stats(stat, pistons_id)

for stat in heat_stats:
    write_player_stats(stat, heat_id)

for stat in spurs_stats:
    write_player_stats(stat, spurs_id)

for stat in kings_stats:
    write_player_stats(stat, kings_id)

for stat in raptors_stats:
    write_player_stats(stat, raptors_id)
import requests
from object import session
import model
Player = model.CurrentPlayer

magic_id = "583ed157-fb46-11e1-82cb-f4ce4684ea4c"
pistons_id = "583ec928-fb46-11e1-82cb-f4ce4684ea4c"
heat_id = "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"  # type: str
spurs_id = "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"
kings_id = "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"
raptors_id = "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"
lakers_id = "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
timberwolves_id = "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"


def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value


def roster_url(game_id):
    head = "https://api.sportradar.us/nba/trial/v5/en/teams/"
    tail = "/profile.json?api_key=dek9px59ega4h4vv3hjuw59p"
    url = head + game_id + tail
    return url

def grab_roster(team_id):
    r = requests.get(roster_url(team_id))
    roster = r.json().get("players")
    for p in roster:
        print p
        player = Player()
        player.player_id = p.get("id")
        player.team_id = team_id
        player.first_name = p.get("first_name")
        player.last_name = p.get("last_name")
        player.jersey_number = p.get("jersey_number")
        player.points = "-"
        player.assists = "-"
        player.rebounds = "-"
        player.fg_percent = "-"
        player.played = "-"
        session.add(player)
        session.flush()
        session.commit()

grab_roster(timberwolves_id)
grab_roster(pistons_id)
grab_roster(heat_id)
grab_roster(spurs_id)
grab_roster(kings_id)
grab_roster(raptors_id)
grab_roster(magic_id)
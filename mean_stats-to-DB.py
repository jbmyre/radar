from object import session
import model
Player = model.Player

player_q = session.query(Player).distinct(Player.player_id).group_by(Player.player_id).all()

all_players = []

for player in player_q:
    all_players.append(player.player_id)


def get_all_players_games(p_id):
    games = session.query(Player).filter_by(player_id=p_id).all()
    points = []
    rebounds = []
    assists = []
    fg_percent = []
    played = 0
    for game in games:
        points.append(game.points)
        rebounds.append(game.rebounds)
        assists.append(game.assists)
        fg_percent.append(game.fg_percent)
        if game.points != 0 or game.points != 0 or game.assists != 0 or game.rebounds != 0 or game.fg_percent != 0:
            played = played + 1

    adv = model.AveragePlayer()
    adv.first_name = games[0].first_name
    adv.last_name = games[0].last_name
    adv.jersey_number = games[0].jersey_number
    adv.player_id = p_id
    adv.team_id = games[0].team_id
    adv.points = reduce(lambda x, y: x + y, points) / len(points)
    adv.rebounds = reduce(lambda x, y: x + y, rebounds) / len(rebounds)
    adv.assists = reduce(lambda x, y: x + y, assists) / len(assists)
    adv.fg_percent = reduce(lambda x, y: x + y, fg_percent) / len(fg_percent)
    adv.played =played
    session.add(adv)
    session.flush()
    session.commit()


for p in all_players:
    get_all_players_games(p)

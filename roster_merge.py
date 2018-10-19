from object import session
import model
CurrentPlayer = model.CurrentPlayer
AdvPlayer = model.AveragePlayer
FinalPlayer = model.FinalPlayer


adv_q = session.query(AdvPlayer).all()
current_q = session.query(CurrentPlayer).all()

for player in current_q:

    p_id = player.player_id
    t_id = player.team_id
    adv_player = session.query(AdvPlayer).filter_by(player_id=p_id).first()

    if adv_player is not None:
        first_name = adv_player.first_name
        last_name = adv_player.last_name
        jersey_number = adv_player.jersey_number
        player_id = adv_player.player_id
        team_id = adv_player.team_id
        points = str(adv_player.points)
        rebounds = str(adv_player.rebounds)
        assists = str(adv_player.assists)
        fg_percent = str(adv_player.fg_percent)
        played = str(adv_player.played)
    else:
        first_name = player.first_name
        last_name = player.last_name
        jersey_number = player.jersey_number
        player_id = player.player_id
        team_id = player.team_id
        points = player.points
        rebounds = player.rebounds
        assists = player.assists
        fg_percent = player.fg_percent
        played = player.played

    f_player = FinalPlayer()
    f_player.first_name = first_name
    f_player.last_name = last_name
    f_player.jersey_number = jersey_number
    f_player.player_id = player_id
    f_player.team_id = team_id
    f_player.points = points
    f_player.rebounds = rebounds
    f_player.assists = assists
    f_player.fg_percent = fg_percent
    f_player.played = played
    session.add(f_player)
    session.flush()
    session.commit()















from object import session
import model
from sqlalchemy import desc
Player = model.FinalPlayer
Team = model.Team

magic_id = "583ed157-fb46-11e1-82cb-f4ce4684ea4c"
pistons_id = "583ec928-fb46-11e1-82cb-f4ce4684ea4c"
heat_id = "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"  # type: str
spurs_id = "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"
kings_id = "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"
raptors_id = "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"
lakers_id = "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
timberwolves_id = "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"

lakers_q = session.query(Player).filter_by(team_id=lakers_id).order_by(desc(Player.jersey_number)).all()
pistons_q = session.query(Player).filter_by(team_id=pistons_id).order_by(desc(Player.jersey_number)).all()
heat_q = session.query(Player).filter_by(team_id=heat_id).order_by(desc(Player.jersey_number)).all()
spurs_q = session.query(Player).filter_by(team_id=spurs_id).order_by(desc(Player.jersey_number)).all()
kings_q = session.query(Player).filter_by(team_id=kings_id).order_by(desc(Player.jersey_number)).all()
raptors_q = session.query(Player).filter_by(team_id=raptors_id).order_by(desc(Player.jersey_number)).all()
timberwolves_q = session.query(Player).filter_by(team_id=timberwolves_id).order_by(desc(Player.jersey_number)).all()
magic_q = session.query(Player).filter_by(team_id=magic_id).order_by(desc(Player.jersey_number)).all()


def write_txt(team1,team1_id, team2, team2_id):
    team1_q = session.query(Team).get(team1_id)
    team2_q = session.query(Team).get(team2_id)
    home_code = "100"
    away_code = "200"
    if team1_q.home:
        home_team = team1_q
        away_team = team2_q
        home = team1
        away = team2
    else:
        home_team = team2_q
        away_team = team2_q
        home = team2
        away = team1

    team1_abbr = home_team.name[:3]
    team2_abbr = away_team.name[:3]
    file_name = "text_files/{:s}{:s}_FSN.txt".format(team1_abbr.upper(),team2_abbr.upper())
    file = open(file_name,'w')
    file.close()
    home_template1 = "1019910"
    home_template2 = "1019911"
    away_template1 = "2019910"
    away_template2 = "2019911"
    with open(file_name, 'a') as f:

        for player in home:
            home_line1 = "W\{:s}{:s}10\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\October ({:s} Gms)\\".format(home_code, player.jersey_number, home_template1 ,player.jersey_number,player.first_name, player.last_name, str(player.points), str(player.rebounds), str(player.assists) , str(player.played)) + "\\"
            f.write(home_line1)
            f.write('\n')


        for player in away:
            away_line1 = "W\{:s}{:s}10\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\October ({:s} Gms)\\".format(away_code, player.jersey_number, away_template1, player.jersey_number,player.first_name, player.last_name, str(player.points), str(player.rebounds), str(player.assists), str(player.played)) + "\\"
            f.write(away_line1)
            f.write('\n')

        for player in home:
            home_line2 = "W\{:s}{:s}11\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\October ({:s} Gms)\\".format(home_code, player.jersey_number, home_template2 ,player.jersey_number,player.first_name, player.last_name, str(player.points), str(player.rebounds), str(player.fg_percent), str(player.played)) + "\\"
            f.write(home_line2)
            f.write('\n')


        for player in away:
            away_line2 = "W\{:s}{:s}11\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\{:s}\October ({:s} Gms)\\".format(away_code, player.jersey_number, away_template2, player.jersey_number,player.first_name, player.last_name, str(player.points), str(player.rebounds), str(player.fg_percent), str(player.played)) + "\\"
            f.write(away_line2)
            f.write('\n')


write_txt(magic_q,magic_id,pistons_q,pistons_id)
write_txt(heat_q,heat_id,spurs_q,spurs_id)
write_txt(kings_q,kings_id,raptors_q,raptors_id)
write_txt(lakers_q,lakers_id, timberwolves_q, timberwolves_id)
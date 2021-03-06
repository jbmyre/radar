from sqlalchemy import orm
from sqlalchemy import schema, types

metadata = schema.MetaData()

team_table = schema.Table('team', metadata,
                          schema.Column('id', types.Unicode(255), primary_key=True),
                          schema.Column('name', types.Unicode(255)),
                          schema.Column('home', types.Boolean, default=False),
                          schema.Column('game_count', types.Integer),
                          )

player_table = schema.Table('player', metadata,
                            schema.Column('id', types.Integer, autoincrement=True, primary_key=True),
                            schema.Column('player_id', types.Unicode(255)),
                            schema.Column('team_id', types.Unicode(255),
                                          schema.ForeignKey('team.id'), nullable=False),
                            schema.Column('first_name', types.Unicode(255)),
                            schema.Column('last_name', types.Unicode(255)),
                            schema.Column('jersey_number', types.Unicode(255)),
                            schema.Column('points', types.Integer),
                            schema.Column('rebounds', types.Integer),
                            schema.Column('assists', types.Integer),
                            schema.Column('fg_percent', types.Integer),
                            )

current_player_table = schema.Table('current_player', metadata,
                            schema.Column('id', types.Integer, autoincrement=True, primary_key=True),
                            schema.Column('player_id', types.Unicode(255)),
                            schema.Column('team_id', types.Unicode(255),
                                          schema.ForeignKey('team.id'), nullable=False),
                            schema.Column('first_name', types.Unicode(255)),
                            schema.Column('last_name', types.Unicode(255)),
                            schema.Column('jersey_number', types.Unicode(255)),
                            schema.Column('points', types.Unicode(255)),
                            schema.Column('rebounds', types.Unicode(255)),
                            schema.Column('assists', types.Unicode(255)),
                            schema.Column('fg_percent', types.Unicode(255)),
                            schema.Column('played', types.Unicode(255)),
                            )

final_player_table = schema.Table('final_stats', metadata,
                            schema.Column('id', types.Integer, autoincrement=True, primary_key=True),
                            schema.Column('player_id', types.Unicode(255)),
                            schema.Column('team_id', types.Unicode(255)),
                            schema.Column('first_name', types.Unicode(255)),
                            schema.Column('last_name', types.Unicode(255)),
                            schema.Column('jersey_number', types.Unicode(255)),
                            schema.Column('points', types.Unicode(255)),
                            schema.Column('rebounds', types.Unicode(255)),
                            schema.Column('assists', types.Unicode(255)),
                            schema.Column('fg_percent', types.Unicode(255)),
                            schema.Column('played', types.Unicode(255)),
                            )

average_player_table = schema.Table('player_average', metadata,
                                    schema.Column('id', types.Integer, autoincrement=True, primary_key=True),
                                    schema.Column('player_id', types.Unicode(255)),
                                    schema.Column('team_id', types.Unicode(255),
                                                  schema.ForeignKey('team.id'), nullable=False),
                                    schema.Column('first_name', types.Unicode(255)),
                                    schema.Column('last_name', types.Unicode(255)),
                                    schema.Column('jersey_number', types.Unicode(255)),
                                    schema.Column('points', types.Integer),
                                    schema.Column('rebounds', types.Integer),
                                    schema.Column('assists', types.Integer),
                                    schema.Column('fg_percent', types.Integer),
                                    schema.Column('played', types.Integer),
                                    )


class Team(object):
    pass


class Player(object):
    pass


class AveragePlayer(object):
    pass


class CurrentPlayer(object):
    pass


class FinalPlayer(object):
    pass


orm.mapper(Team, team_table, properties={
    'players': orm.relation(Player, backref='team')
})

orm.mapper(Player, player_table)

orm.mapper(AveragePlayer, average_player_table)

orm.mapper(CurrentPlayer, current_player_table)

orm.mapper(FinalPlayer, final_player_table)

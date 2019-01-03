import random
import sqlite3

def add_random_games(num_games=30):
    with sqlite3.connect('recess.db')as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        game_types = ['basketball', 'dodgeball', 'football', 'frisbee', 'hide_and_seek',
                      'hockey', 'running', 'soccer', 'table_tennis', 'tennis', 'volleyball']
        locations =
        query = """SELECT id FROM users"""
        cur.execute(query)
        users = [dict(row)['id'] for row in cur.fetchall()]
        query = """SELECT DISTINCT location FROM games"""
        cur.execute(query)
        locations = [dict(row)['location'] for row in cur.fetchall()]
        if len(game_types) == 0:
            print('Found 0 game types, not generating games')

        else:
            for i in num_games:
                random values...
                query = """INSERT into games (game_type, game_name, game_day, start_time, 
                location, min_players, max_players, num_teams) 
                values , '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".\
                            format(game_type, game_name, game_day, start_time, location, min_players, max_players, num_teams)
                cur.execute(query)
                con.commit()


if __name__ == '__main__':
    add_random_games()

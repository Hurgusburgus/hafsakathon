import sqlite3

def randomly_add_users_to_games():
    from random import randint
    with sqlite3.connect('recess.db')as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        query = """SELECT id_game, creator_id, min_players, max_players
        FROM games"""
        cur.execute(query)
        games = [dict(row) for row in cur.fetchall()]
        query = """SELECT id FROM users"""
        cur.execute(query)
        users = [dict(row)['id'] for row in cur.fetchall()]
        for game in games:
            if game['min_players'] and game['max_players']:
                num_players_to_add = randint(game['min_players'] - 1,
                                             game['max_players'] - 1)
                for player in range(num_players_to_add):
                    users_added = [game['creator_id']]
                    random_player = users[randint(0, len(users) - 1)]
                    if random_player not in users_added:
                        users_added.append(random_player)
                        query = """INSERT INTO users_games
                        (game_id, user_id)
                        VALUES ('{}', '{}')""".format(game['id_game'], random_player)
                        cur.execute(query)
            con.commit()

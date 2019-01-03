import sqlite3

def randomly_add_users_to_games():
    from random import randint
    with sqlite3.connect('recess.db')as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        query = """SELECT id_game, min_players, max_players
        FROM games"""
        cur.execute(query)
        games = [dict(row) for row in cur.fetchall()]



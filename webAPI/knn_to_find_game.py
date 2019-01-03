from bottle import route
import json
import sqlite3


@route('/suggest_games/<user_id>')
def suggest_game(user_id):
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            query = "SELECT * FROM games WHERE user_id = {}".format(game_id)
            cur.execute(query)
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})

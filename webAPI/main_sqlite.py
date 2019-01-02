from bottle import run, route, get, post, delete, put, request, template, response, hook
import bottle
import os
import pymysql
import json
from requests import request
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'  # * in case you want to be accessed via any website
        return func(*args, **kwargs)

    return wrapper



@route('/users/<id>')
def get_user(id):
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            query = "SELECT * FROM users WHERE id = {}".format(id)
            cur.execute(query)
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(output)

    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@post('/index')
def add_user_to_users():
    try:
        with sqlite3.connect('recess.db')as con:
            username = request.forms.get("username")
            firstname = request.forms.get("firstname") if request.forms.get("firstname") else None
            lastname = request.forms.get("lastname") if request.forms.get("lastname") else None
            birth = request.forms.get("birth")
            sex = request.forms.get("sex")
            city = request.forms.get("city")
            phone = request.forms.get("phone") if request.forms.get("phone") else None
            email = request.forms.get("email")
            pass_ = request.forms.get("pass")
            description = request.forms.get("description") if request.forms.get("description") else None
            reg_date = request.forms.get("reg_date") if request.forms.get("reg_date") else None
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            query = "INSERT into users (username, firstname, lastname, birth, sex, city, phone, email, pass_, description, reg_date)" \
                    " values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                 username, firstname, lastname, birth, sex, city, phone, email, pass_, description, reg_date)
            cur.execute(query)
            con.commit()
            user_query = "SELECT * FROM users where id = {}".format(
                id)
            cur.execute(user_query)
            response.status = 201
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))

    except Exception as e:
        return e
        #return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})



@delete('/users/<id:int>')
def remove_user_from_user(id):
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            sql = ('DELETE FROM users WHERE id = {}'.format(id))
            cur.execute(sql)
            con.commit()
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(output)
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@delete('/games_users/<user_id:int>/<game_id:int>')
def remove_from_game(user_id, game_id):
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            sql = ('DELETE FROM games_users WHERE game_id = {}'
                   .format(user_id, game_id))
            cur.execute(sql)
            con.commit()
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@route('/games/<game_id>')
def get_game(game_id):
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            query = "SELECT * FROM games WHERE game_id = {}".format(game_id)
            cur.execute(query)
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})



@post('/games')
def add_game():
    try:
        with sqlite3.connect('recess.db')as con:
            game_id = request.forms.get("game_id")
            game_type = request.forms.get("game_type") if request.forms.get("game_type") else None
            game_name = request.forms.get("game_name") if request.forms.get("game_name") else None
            game_day = request.forms.get("game_day")
            start_time = request.forms.get("start_time")
            location = request.forms.get("location") if request.forms.get("location") else None
            min_players = request.forms.get("min_players")
            max_players = request.forms.get("max_players") if request.forms.get("max_players") else None
            num_teams = request.forms.get("num_teams")
            query = "INSERT into games (game_id) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                game_id, game_type, game_name, game_day, start_time, location, min_players, max_players, num_teams)
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            games_query = "SELECT * FROM games where id = {}".format(
                game_id)
            cur.execute(games_query)
            response.status = 201
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})




@route('/games/all')
@allow_cors
def get_all_games():
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            query = "SELECT * FROM games"
            cur.execute(query)
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)
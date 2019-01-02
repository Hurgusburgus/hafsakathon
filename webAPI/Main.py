from bottle import run, route, get, post, delete, put, request, template, response
import bottle
import os
import pymysql
import json
from requests import request

bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)))

connection = pymysql.connect(host='db4free.net',
                             user='recess',
                             password='recess123',
                             db='recess',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'  # * in case you want to be accessed via any website
        return func(*args, **kwargs)

    return wrapper



@route('/users/<user_id>')
def get(user_id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE id = {}".format(user_id)
            cursor.execute(query)
            return json.dumps(str(cursor.fetchone()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@post('/index')
@allow_cors
def add_user_to_users():
    try:
        with connection.cursor() as cursor:
            id = request.forms.get("id")
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

            query = "INSERT into users values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                id, username, firstname, lastname, birth, sex, city, phone, email, pass_, description, reg_date)
            cursor.execute(query)
            connection.commit()
            user_query = "SELECT * FROM users where id = {}".format(id)
            cursor.execute(user_query)
            response.status = 201
            return json.dumps(str(cursor.fetchone()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})

@post('/games/add_users')
@allow_cors
def add_user_to_game():
    try:
        with connection.cursor() as cursor:
            user_id = request.forms.get("user_id")
            game_id = request.forms.get("game_id")

            is_in_game_querry = """SELECT *
                            FROM users
                            WHERE id == {}""".format(user_id)

            cursor.execute(is_in_game_querry)
            is_in_game = str(cursor.fetchone())
            if is_in_game:
                return "User Already in Game!"


            curr_players_query = """ SELECT  COUNT(*) 
                             FROM  games_useres
                             WHERE game_id == {}""".format(game_id)

            cursor.execute(curr_players_query)
            curr_players = int(cursor.fetchone())

            max_players_querry = """ SELECT max_players
                                     FROM games
                                     WHERE game_id == {}""".format(game_id)

            cursor.execute(curr_players_query)
            max_players = int(cursor.fetchone())

            if curr_players > max_players:
                return "Cant Add user, game reached "\
                        "maximum users limit for the game"

            insertion_query = """INSERT INTO games_users( game_id, user_id)
                                 VALUES({}, {})""".format(game_id,user_id)

            return "user {} inserted into game {}".format(user_id,game_id)
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})








# MVP2
# @put('/users/<id>')
# def update(id):
#     try:
#         with connection.cursor() as cursor:
#             newid = request.forms.get('id')
#             game_id = request.forms.get('game_id')
#             sql = "UPDATE users SET id=%s, game_id=%d, WHERE id = '{}'".format(
#                 newid, game_id, id)
#             cursor.execute(sql)
#             connection.commit()
#             response.status = 201
#             return json.dumps(cursor.fetchone())
#     except:
#         return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@delete('/users/<id:int>')
@allow_cors
def remove_user_from_users(id):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM games_users WHERE user_id = {}'.format(id))
            cursor.execute(sql)
            sql = ('DELETE FROM users WHERE id = {}'.format(id))
            cursor.execute(sql)
            connection.commit()
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@delete('/games_users/<user_id:int>/<game_id:int>')
@allow_cors
def remove_from_game(user_id, game_id):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM games_users WHERE user_id = {} AND game_id = {}'
                   .format(user_id, game_id))
            cursor.execute(sql)
            connection.commit()
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})

# MVP3?
# @get('/users')
# def getAll():
#     try:
#         with connection.cursor() as cursor:
#             query = "SELECT * FROM users"
#             cursor.execute(query)
#             return json.dumps(cursor.fetchall())
#     except:
#         return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})

@route('/games/<game_id>')
@allow_cors
def get_all_games(game_id):
    try:
        with connection.cursor() as cursor:
            # add tables
            query = "SELECT * FROM games WHERE game_id = {}".format(game_id)
            cursor.execute(query)
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@post('/games')
@allow_cors
def addgame():
    try:
        with connection.cursor() as cursor:
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
            cursor.execute(query)
            connection.commit()
            games_query = "SELECT * FROM games where id = {}".format(
                game_id)
            cursor.execute(games_query)
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@delete('/games/<game_id:int>')
@allow_cors
def remove_game(game_id):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM games WHERE game_id = {}'.format(game_id))
            cursor.execute(sql)
            connection.commit()
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@route('/games/all')
@allow_cors
def get_all_games():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM games"
            cursor.execute(query)
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)

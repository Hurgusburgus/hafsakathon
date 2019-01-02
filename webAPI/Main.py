from bottle import run, route, get, post, delete, put, request, template, response, hook
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

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

@route('/', method = 'OPTIONS')
@route('/<path:path>', method = 'OPTIONS')
def options_handler(path = None):
    return


@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@route('/users/<id>')
def get(id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE id = {}".format(id)
            cursor.execute(query)
            return json.dumps(str(cursor.fetchone()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@post('/index')
def add():
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
            user_query = "SELECT * FROM users where id = {}".format(
                id)
            cursor.execute(user_query)
            response.status = 201
            return json.dumps(str(cursor.fetchone()))
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
def remove(id):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM users WHERE id = {}'.format(id))
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
def get(game_id):
    try:
        with connection.cursor() as cursor:
            # add tables
            query = "SELECT * FROM games WHERE game_id = {}".format(game_id)
            cursor.execute(query)
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})



@post('/games')
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
def remove(game_id):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM games WHERE game_id = {}'.format(game_id))
            cursor.execute(sql)
            connection.commit()
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@route('/games/all')
def getAll():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM games"
            cursor.execute(query)
            return json.dumps(str(cursor.fetchall()))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


if __name__ == '__main__':
    run(host='localhost', port=7000, debug=True)

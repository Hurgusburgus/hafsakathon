from bottle import run, route, get, post, delete, put
import bottle
import os
import pymysql
from pymysql.connections import Connection
import json
from requests import request


bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(__file__)))

connection = pymysql.connect(host='db4free.net',
                             user='recess',
                             password='recess123',
                             db='recess',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


@get('/users/<id>')
def get(id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE id = {}".format(id)
            cursor.execute(query)
            return json.dumps(cursor.fetchone())
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@post('/users')
def add():
    try:
        with connection.cursor() as cursor:
            id = request.json.get("id")
            # ADD ALL THE FIELDS WE NEED TO GET FOR EACH USER

            query = "INSERT into users (id) values ('{}', '{}')".format(
                id)
            cursor.execute(query)
            connection.commit()
            student_query = "SELECT * FROM users where id = '{}'".format(
                id)
            cursor.execute(student_query)
            # response.status = 201
            return json.dumps(cursor.fetchone())
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
            return json.dumps(cursor.fetchall())
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


@get('/games/<game_id>')
def get(game_id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE game_id = {}".format(
                game_id)
            cursor.execute(query)
            return json.dumps(cursor.fetchall())
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@post('/games')
def addgame():
    try:
        with connection.cursor() as cursor:
            game_id = request.json.get("game_id")
            query = "INSERT into games (game_id) values ('{}')".format(
                game_id)
                # ADD ALL THE GAME COLUMNS 
            cursor.execute(query)
            connection.commit()
            games_query = "SELECT * FROM games"
            cursor.execute(games_query)
            return json.dumps(cursor.fetchall())
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@delete('/games/<game_id:int>')
def remove(game_id):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM games WHERE game_id = {}'.format(game_id))
            cursor.execute(sql)
            connection.commit()
            return json.dumps(cursor.fetchall())
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@get('/games/all')
def getAll():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM games"
            cursor.execute(query)
            return json.dumps(cursor.fetchall())
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


if __name__ == '__main__':
    run(host='localhost', port=7000, debug=True)

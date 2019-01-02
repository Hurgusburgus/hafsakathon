from bottle import run, route, get, post, delete, put, request, template, response, hook

import json
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

            #postdata = request.body.read()
            #username = json.loads(postdata)["username"]
            username = request.forms.get('username')
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
            query = "INSERT into users (username, firstname, lastname, birth, sex, city, phone, email, pass, description, reg_date)" \
                    " values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                 username, firstname, lastname, birth, sex, city, phone, email, pass_, description, reg_date)
            cur.execute(query)
            con.commit()

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
            game_type = request.forms.get("game_type") #if request.forms.get("game_type") else None
            game_name = request.forms.get("game_name") #if request.forms.get("game_name") else None
            game_day = request.forms.get("game_day")
            start_time = request.forms.get("start_time")
            location = request.forms.get("location") if request.forms.get("location") else None
            min_players = request.forms.get("min_players") if request.forms.get("min_players") else None
            max_players = request.forms.get("max_players") if request.forms.get("max_players") else None
            num_teams = request.forms.get("num_teams")
            query = """INSERT into games (game_type, game_name, game_day, start_time, location, min_players, max_players, num_teams) 
                    values , '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".\
                format(game_type, game_name, game_day, start_time, location, min_players, max_players, num_teams)
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            #games_query = "SELECT * FROM games where id = {}".format(game_id)
            #cur.execute(games_query)
            response.status = 201
            output = [dict(row) for row in cur.fetchall()]
            cur.close()
            return json.dumps(str(output))
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@route('/search/<game_type>/<date>/<day_of_week>/<hours>/<location>')
def find_games(game_type, date, day_of_week, hours, location):
    """
    For each of the search parameters, pass a value of 'all' if
    it wasn't defined by the user.
    otherwise the parameters are defined as follows:

    game_type: the values of game_type in games table, separated with two dashes --

    date: date string in the format yyyy-mm-dd (e.g. 2019-01-02)

    day_of_week: string with digits of days of week specified by the user (0-6 where 0 is sunday e.g. '014')

    hours: string with four digits for start and finish hour (e.g. '0913')

    location: the values of location in games table, separated with two dashes --
    """
    try:
        with sqlite3.connect('recess.db')as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            sql = 'SELECT * FROM games WHERE 1=1 '
            if game_type != 'all':
                game_type = '(' + str(game_type.split('--'))[1:-1] + ')'
                sql += f'AND game_type in {game_type} '
            if date != 'all':
                date = "'" + date + "'"
                sql += f'AND game_day = date({date}) '
            elif day_of_week != 'all':  # check day of week only if date wasn't specified
                day_of_week = '(' + str([d for d in day_of_week])[1:-1] + ')'
                sql += f"AND strftime('%w', game_day) in {day_of_week} "
            if hours != 'all':
                start = hours[:2]
                finish = hours[2:]
                sql += f"AND start_time between {start} AND {finish} "
            if location != 'all':
                location = '(' + str(location.split('--'))[1:-1] + ')'
                sql += f'AND location in {location} '
            cur.execute(sql)
            output = [dict(row) for row in cur.fetchall()]
            return json.dumps(str(output))

    except Exception:
        #raise
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})

    finally:
        cur.close()




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
            return json.dumps(output)
    except:
        return json.dumps({"STATUS": "ERROR", "MSG": "Internal error", "CODE": 500})


@route('/locations')
@allow_cors
def get_locations():
    return ['Tel-Aviv','Jerusalem', 'Netanya', 'Jaffa']


@route('/game_types')
@allow_cors
def get_locations():
    return ["basketball", "dodgeball", "frisbee", "hide_and_seek", "hockey",
            "running", "soccer", "table_tennis", "tennis", "volleyball",
            "other"]






if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)
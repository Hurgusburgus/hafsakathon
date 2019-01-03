import sqlite3

DATABASE = 'recess.db'
def add_random_games(num_games=30):
    from random import randint
    with sqlite3.connect(DATABASE)as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        game_types = ['basketball', 'dodgeball', 'football', 'frisbee', 'hide_and_seek',
                      'hockey', 'running', 'soccer', 'table_tennis', 'tennis', 'volleyball']
        locations = ['jerusalem', 'tel aviv', 'netanya', 'haifa']
        game_names = ['maccabies', 'lions', 'fun game', 'newbies', 'champions', 'hello :)',
                      'something-something', 'creativity', 'itc', 'fellows', 'stuff',
                      'bring it on', 'lets random stuff', 'kaduregel', 'kadursal',
                      'whatever', 'game', 'my game', 'please join', 'cool project', 'recess']
        query = """SELECT id FROM users"""
        cur.execute(query)
        users = [dict(row)['id'] for row in cur.fetchall()]
        if len(users) == 0:
            print('Found 0 users, not generating games')
        else:
            for i in range(num_games):
                creator_id = users[randint(0, len(users) - 1)]
                game_type = game_types[randint(0, len(game_types) - 1)]
                game_name = game_names[randint(0, len(game_names) - 1)]
                if randint(0, 1) == 0:
                    game_name = 'user' + str(creator_id) + ' ' + game_name
                day = str(randint(1, 28))
                month = str(randint(1, 12))
                year = '2019'
                game_day = year + '-' + month + '-' + day
                start_time = randint (7, 23)
                location = locations[randint(0, len(locations) - 1)]
                min_players = randint(4, 12)
                max_players = randint(min_players, min_players * 3)
                num_teams = randint(2, 4)
                query = """INSERT into games (creator_id, game_type, game_name, game_day, start_time, 
                location, min_players, max_players, num_teams) 
                values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".\
                            format(creator_id, game_type, game_name, game_day, start_time,
                                   location, min_players, max_players, num_teams)
                cur.execute(query)
                con.commit()

def show_games():
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from games")
        for row in cur.fetchall():
            print(row)


if __name__ == '__main__':
    add_random_games()

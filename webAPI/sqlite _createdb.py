import sqlite3
from generate_random_games import add_random_games
from randomly_add_users_to_games import randomly_add_users_to_games
from generate_users_sql import populate_users

DATABASE = 'recess.db'


def create_users_table():
    """
    A method that create the "users" sql table with the following properties:
    id,username, firstname, lastname ,birth, sex, city, phone, email, pass,
    description, reg_date (registration date)
    :return: None
    """
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS users""")
        con.commit()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        username text NOT NULL,
                        firstname text,
                        lastname text,
                        birth DATE,
                        sex text DEFAULT 'N',
                        city text NOT NULL,
                        phone text,
                        email text NOT NULL,
                        pass text NOT NULL,
                        description text,
                        reg_date TIMESTAMP);
                    """)
        con.commit()
        cur.close()

def create_games_table():
    """
    A method that create the 'games' table in the database with the following
    properties:
                id_game, creator_id,game_name, game_day, start_time, location,
                min_players, max_players, num_teams

    :return: None
    """
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS games""")
        con.commit()
        cur.execute("""CREATE TABLE IF NOT EXISTS games (
                        game_id integer PRIMARY KEY AUTOINCREMENT,
                        creator_id integer NOT NULL,
                        game_type text,
                        game_name text,
                        game_day DATE NOT NULL,
                        start_time text NOT NULL,
                        location text,
                        min_players integer NOT NULL DEFAULT 2,
                        max_players int,
                        num_teams integer DEFAULT 0,
                        FOREIGN KEY (creator_id) REFERENCES users(id));
                     """)

        con.commit()
        cur.close()

def create_users_games():
    """
    A method that create the table 'users_games' which in a week entity
    describing the users which are in active games
    the table consists of two foreign keys "user_id" which refrences the id
    of a user in the users table, and the "game_id" which refrences the id of a
    game in the "games" table.
    :return: None
    """
    with sqlite3.connect('recess.db')as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS users_games""")
        con.commit()
        query = """CREATE TABLE IF NOT EXISTS `users_games`
                    (`game_id` int,`user_id` int,
                      FOREIGN KEY (`user_id`) REFERENCES users(`id`),
                      FOREIGN KEY (`game_id`) REFERENCES games(`game_id`))
                """
        cur.execute(query)
        con.commit()
        cur.close()



def get_schema():
    ""
    with sqlite3.connect('recess.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM sqlite_master WHERE type='table'""")
        x = cur.fetchall()
        print(x[:][4])


def show_users(n):
    """
    A method that displays a number of entries from the head of the users table
    :param n: the number of entries to display
    :return: None
    """
    print("users content:")
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from users limit {}".format(n))
        for row in cur.fetchall():
            print(row)


def show_games(n):
    """
    A method that displays a number of entries from the head of the games table
    :param n: the number of entries to display
    :return: None
    """
    print("games content:")
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from games limit {}".format(n))
        for row in cur.fetchall():
            print(row)


def show_users_games(n):
    """
    A method that displays a number of entries from the head of the user-games
    table
    :param n: the number of entries to display
    :return: None
    """
    print("user_games content:")
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from users_games limit {}".format(n))
        for row in cur.fetchall():
            print(row)


def populate_tables(n_players,n_games,display_num):
    """
    A method that populates the table of the current database with mock values
    generated randomly
    :param n_players: the number of users to generate and populate the users
    table with
    :param n_games: the number of games to generate and populate the games table
    with
    :param display_num: the number of entries to display from each table after
    it was populated
    :return: None
    """
    populate_users(n_players)
    show_users(display_num)
    add_random_games(n_games)
    show_games(display_num)
    randomly_add_users_to_games()
    show_users_games(display_num)


def main():
    create_users_table()
    create_games_table()
    create_users_games()
    populate_tables(n_players=200,n_games=200,display_num=5)
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("""SELECT games.id_game, games.creator_id, users_games.user_id, users.username,
                    users.firstname, users.lastname, users.birth,
                    users.sex, users.city, users.phone, users.email, users.description
                    FROM games
                    INNER JOIN users_games ON users_games.game_id = games.id_game
                    INNER JOIN users ON users_games.user_id = users.id
                    where id_game = {}
                    """.format(1))
        for row in cur.fetchall():
            print(row)


if __name__ == "__main__":
    main()

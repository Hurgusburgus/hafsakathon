import sqlite3
from generate_random_games import add_random_games
from randomly_add_users_to_games import randomly_add_users_to_games
from generate_users_sql import populate_users

DATABASE = 'recess.db'


def create_users_table():
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
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS games""")
        con.commit()
        cur.execute("""CREATE TABLE IF NOT EXISTS games (
                        id_game integer PRIMARY KEY AUTOINCREMENT,
                        creator_id integer NOT NULL,
                        game_type text,
                        game_name text,
                        game_day DATE NOT NULL,
                        start_time text NOT NULL,
                        location text,
                        min_players integer NOT NULL DEFAULT 2,
                        max_players integers,
                        num_teams integer DEFAULT 0,
                        FOREIGN KEY (creator_id) REFERENCES users(id));
                     """)

        con.commit()
        cur.close()

def create_users_games():
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
    with sqlite3.connect('recess.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM sqlite_master WHERE type='table'""")
        x = cur.fetchall()
        print(x[:][4])


def show_users(n):
    print("users content:")
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from users limit {}".format(n))
        for row in cur.fetchall():
            print(row)


def show_games(n):
    print("games content:")
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from games limit {}".format(n))
        for row in cur.fetchall():
            print(row)


def show_users_games(n):
    print("user_games content:")
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()
        cur.execute("select * from users_games limit {}".format(n))
        for row in cur.fetchall():
            print(row)



def populate_tables():
    populate_users(200)
    show_users(5)
    add_random_games(200)
    show_games(5)



def main():
    create_users_table()
    create_games_table()
    create_users_games()
    populate_tables()

    #create_users_games()
    #get_schema()


if __name__ == "__main__":
    main()

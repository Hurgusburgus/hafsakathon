import sqlite3


def create_users_table():
    with sqlite3.connect('recess.db')as con:
        cur = con.cursor()
        # crate table
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
        reg_date TIMESTAMP
        );
        """)
        con.commit()
        cur.close()

def create_games_table():

with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    # crate table
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
    FOREIGN KEY (creator_id) REFERENCES users(id)
    );
    """)

        con.commit()
        cur.close()

def useres_insert():
    with sqlite3.connect('recess.db')as con:
        cur = con.cursor()
        # crate table
        cur.execute("""INSERT INTO users (username,firstname, lastname,birth,sex,
                                          city,phone,email,pass,description,
                                          reg_date)
                       VALUES ('me','my','name',05/03/1991,'female','meitar',
                                0544959583,'me@gmail.com',123456,'hello',
                                02/01/2019);
                    """)

    cur.execute("""INSERT INTO users (
    username,
    firstname,
    lastname,
    birth,
    sex,
    city,
    phone,
    email,
    pass,
    description,
    reg_date)

    VALUES (
    'smadar',
    'smadar',
    'danon',
    05/05/1994,
    'female',
    'tel aviv',
    05555555,
    'smadar@gmail.com',
    123456,
    'hello',
    02/01/2019
    );
    """)


        # crate table
        cur.execute("""INSERT INTO users (
        username,
        firstname,
        lastname,
        birth,
        sex,
        city,
        phone,
        email,
        pass)
    
        VALUES (
        'barb',
        'barbara',
        'cohen',
        date('1994-07-07'),
        'female',
        'tel aviv',
        054466771,
        'barb@gmail.com',
        123456
        );
        """)


        con.commit()

        cur = con.cursor()
        cur.execute("""SELECT* FROM users""")
        rows = cur.fetchall()
        #     print(rows)
        print(rows)

        cur.close()




with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    # crate table

    con.commit()
    cur.close()
#





def insert_games():
    with sqlite3.connect('recess.db')as con:
        cur = con.cursor()
        # crate table
        cur.execute("""INSERT INTO games (
        game_type,
        game_name,
        game_day,
        start_time,
        location,
        max_players)
    
        VALUES (
        'volleyball',
        'the good guys',
        05/01/2019,
        17,
        'jerusalem',
        6
        
        );
        """)

        cur.execute("""INSERT INTO games (
        game_type,
        game_name,
        game_day,
        start_time,
        location,
        max_players)
    
        VALUES (
        'soccer',
        'winners',
        05/01/2019,
        18,
        'tel aviv',
        6
    
        );
        """)

        cur.execute("""INSERT INTO games (
        game_type,
        game_name,
        game_day,
        start_time,
        location,
        max_players)
    
        VALUES (
        'table tennis',
        'kids',
        04/01/2019,
        18,
        'jerusalem',
        15
    
        );
        """)

        cur.execute("""SELECT* FROM games""")
        rows = cur.fetchall()
        #     print(rows)
        print(rows)

        VALUES (
        'soccer',
        'team',
        date('1994-07-07'),
        'bla',
        'jerusalem',
        5
        );
        """)

    cur.close()


def create_users_games():
    with sqlite3.connect('recess.db')as con:
        cur = con.cursor()
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
        print(x[3][4])

def main():
    #create_users_games()
    get_schema()


if __name__ == "__main__":
    main()
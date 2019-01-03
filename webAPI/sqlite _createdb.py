import sqlite3

### create users table
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


### create games table

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

### create users_games table


with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    query = """CREATE TABLE IF NOT EXISTS users_games (
                id integer PRIMARY KEY AUTOINCREMENT,
                game_id integer,
                user_id integer,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (game_id) REFERENCES games(game_id)) 
            """
    cur.execute(query)
    con.commit()
    cur.close()


###########################################################
# insert to the table
###########################################################


with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    cur.execute("""INSERT INTO users (
                    username,
                    city,
                    email,
                    pass)

                    VALUES (
                    'chen123', 
                    'tel aviv',
                    'chen@yahoo.com',
                    'chen123')"""

                )


    con.commit()
    cur.close()


with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    # crate table
    cur.execute("""INSERT INTO games (
    game_type,
    creator_id,
    game_day,
    start_time)
    

    VALUES (
    'volleyball',
    2,
    date('2019-01-07'),
    '17:30')
    """)
    con.commit()
    cur.close()


with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    # crate table
    cur.execute("""INSERT INTO users_games (
    game_id,
    user_id)

    VALUES (
    2,
    3
    );
    """)







with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    cur.execute("""SELECT* FROM users""")
    rows = cur.fetchall()
    #     print(rows)
    print(rows)

    cur.close()

with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    cur.execute("""SELECT* FROM games""")
    rows = cur.fetchall()
    #     print(rows)
    print(rows)

    cur.close()

with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    cur.execute("""SELECT* FROM users_games""")
    rows = cur.fetchall()
    #     print(rows)
    print(rows)

    cur.close()


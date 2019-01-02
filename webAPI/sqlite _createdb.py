import sqlite3

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


with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    # crate table
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
    id_game integer PRIMARY KEY AUTOINCREMENT,
    game_type text,
    game_name text,
    game_day DATE NOT NULL,
    start_time TIME NOT NULL,
    location text,
    min_players integer NOT NULL DEFAULT 2,
    max_players integers,
    num_teams integer DEFAULT 0
    );
    """)


    con.commit()
    cur.close()


with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
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
    pass,
    description,
    reg_date)

    VALUES (
    'me',
    'my',
    'name',
    05/03/1991,
    'female',
    'meitar',
    0544959583,
    'me@gmail.com',
    123456,
    'hello',
    02/01/2019
    );
    """)


    con.commit()
    cur.close()

with sqlite3.connect('recess.db')as con:
    cur = con.cursor()
    cur.execute("""SELECT* FROM users""")
    rows = cur.fetchall()
    #     print(rows)
    print(rows)

    cur.close()


# with sqlite3.connect('recess.db')as con:
#     cur = con.cursor()
#     # crate table
#     cur.execute("""INSERT INTO users (
#     username,
#     firstname,
#     lastname,
#     birth,
#     sex,
#     city,
#     phone,
#     email,
#     pass,
#     description,
#     reg_date)
#
#     VALUES (
#     'me',
#     'my',
#     'name',
#     05/03/1991,
#     'female',
#     'meitar',
#     0544959583,
#     'me@gmail.com',
#     123456,
#     'hello',
#     02/01/2019
#     );
#     """)
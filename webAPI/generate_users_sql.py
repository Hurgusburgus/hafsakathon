import numpy as np
import sqlite3


DATABASE = 'recess.db'
def generate_useres(n):
    firstnames = ["Oren", "Gabe", "Shay", "Smadar", "Guy", "Roman", "Roee",
                  "Matan", "Yotam", "Shir", "Michal", "Yigal", "Neta", "Maya"]
    lastnames =["Chikli", "Rimon", "Danon", "Weinstein", "strauss", "Haim",
                "Tshova", "Amari", "nestrov", "tianov", "Cohen", "Braunstein"
                "Bar", "pier"]
    birth_dates = ["1989-05-22", "2000-04-03", "1982-07-30","1986-10-24",
                   "1994-08-12", "1997-08-15", "2001-06-18", "1996-02-18",
                   "1995-07-15", "1987-08-19","1996-05-01","1983-01-01",
                   "2001-02-05"]
    user_names = ["Superman","Batman","Bob","Batgirl", "Bigbuy", "Aquaman",
                   "Neo", "Trinity", "Ninja", "Dva"]

    sex_op = ["M","F"]
    cities =["Tel-Aviv", "Netanya", "Hafia", "Jaffa", "Jerusalem"]
    pass_ = "password"
    reg_dates = ["2018-01-03","2018-01-02","2018-01-04"]
    email_appen = "@gmail.com"
    phone_start = ["050", "052", "053", "054" ,"055"]

    users = []
    for i in range(n):
        curr_user = {}
        curr_user['username'] = np.random.choice(user_names) + \
                                str(np.random.randint(100))
        curr_user['firstname'] = np.random.choice(firstnames)
        curr_user['lastname'] = np.random.choice(lastnames)
        curr_user['birth'] = np.random.choice(birth_dates)
        curr_user['sex'] = np.random.choice(sex_op)
        curr_user['city'] = np.random.choice(cities)
        curr_user['phone'] = np.random.choice(phone_start) + '-'\
                            + str(np.random.randint(100, 1000)) + '-'\
                            + str(np.random.randint(1000, 10000))
        curr_user['email'] = curr_user['username'] + email_appen
        curr_user['pass'] = pass_ + str(np.random.randint(100))
        curr_user['reg_date'] = np.random.choice(reg_dates)
        users.append(curr_user)

    return users


def useres_insert(given_input):
    with sqlite3.connect(DATABASE)as con:
        cur = con.cursor()

        insertion_querry =\
        """INSERT INTO users (username,firstname, lastname,birth,sex,city,
                              phone,email,pass,reg_date)
                       VALUES ('{username}', '{firstname}' ,'{lastname}', 
                                '{birth}', '{sex}', '{city}', '{phone}', 
                                '{email}', '{pass_}','{reg_date}') """
        for row in given_input:
            query = insertion_querry.format(username=row['username'],
                                            firstname=row['firstname'],
                                            lastname=row['lastname'],
                                            birth=row['birth'],
                                            sex=row['sex'],
                                            city=row['city'],
                                            phone=row['phone'],
                                            email=row['email'],
                                            pass_=row['pass'],
                                            reg_date=row['reg_date'])

            cur.execute(query)
            con.commit()
        cur.close()



def populate_users(n):
    users = generate_useres(n)
    useres_insert(users)



def main():
    populate_users(5)

if __name__ == "__main__":
    main()


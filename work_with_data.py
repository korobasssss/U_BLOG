import sqlite3 as sql

index = 0


def init():
    with sql.connect("users_data.db") as con:
        cur = con.cursor()

        # cur.execute("DROP TABLE users")
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            username TEXT NOT NULL,
            password INTEGER NOT NULL,
            messages TEXT NOT NULL
            )""")
        con.commit()


def add_user(name, surname, username, password):  # TODO защитить пароль
    global index
    with sql.connect("users_data.db") as con:
        cur = con.cursor()

        cur.execute("""SELECT * FROM USERS""")
        users = cur.fetchall()

        index = users[len(users) - 1][0] + 1
        print(index)
        user = (index, name, surname, username, password, "")

        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", user)
        con.commit()


def find_user(username, password):
    with sql.connect("users_data.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM USERS""")
        users = cur.fetchall()

        curr_index = 0
        for user in users:
            if user[3] == username and user[4] == int(password):
                return curr_index
            else:
                curr_index += 1
        return -1


def user_data(i):
    with sql.connect("users_data.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM USERS""")
        users = cur.fetchall()
        return users[i]


def check_user_in_base(username):
    with sql.connect("users_data.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM USERS""")
        users = cur.fetchall()

        for user in users:
            if user[3] == username:
                return True
        return False


def add_message(curr_index, message):
    with sql.connect("users_data.db") as con:
        cur = con.cursor()

        cur.execute("""SELECT * FROM USERS""")
        users = cur.fetchall()
        user_message = users[curr_index][5]
        if user_message != '':
            user_message += '\n' + message
        else:
            user_message = message

        data = (user_message, curr_index)
        cur.execute("UPDATE users SET messages = ? WHERE user_id = ?", data)
        con.commit()


def take_message(curr_index):
    with sql.connect("users_data.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM USERS""")
        users = cur.fetchall()
        message = change_type_from_text_to_arr(users[curr_index][5])
        return message


def change_type_from_arr_to_text(array):
    message = ""
    for el in array:
        message += str(el) + '\n'
    print(message)
    return message


def change_type_from_text_to_arr(string):
    array = string.split('\n')
    return array

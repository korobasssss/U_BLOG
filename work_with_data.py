import sqlite3 as sql

class SQL_Data():
    def __init__(self):
        con = sql.connect("users_data.db")

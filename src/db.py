from sqlite3 import *


class DataBase:

    def __init__(self):
        self.conn = connect('phone_list.db')
        self.c = self.conn.cursor()
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS phone_list (id integer primary key, \
            name text, description text, phone text)')
        self.conn.commit()

    def insert_data(self, name, description, phone):
        self.c.execute('INSERT INTO phone_list (name, description, phone) VALUES (?, ?, ?)',
                       (name, description, phone))
        self.conn.commit()

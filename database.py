import sqlite3

class User:
    def __init__(self, user_id: int, city: str | None=None):
        self.user_id = user_id
        self.city = city
class Database:
    def __init__(self):
        self.cnnection = sqlite3.connect('sqlite.db')
        self.cursor = self.cnnection.cursor()
    def close (self):
        self.cnnection.close()
    def get_user(self, user_id: int) -> User | None:
        query = 'SELECT * FROM user WHERE id = ?'
        args = (user_id,)
        self.cursor.execute(query, args)
        row = self.cursor.fatchone()
        if row is None:
            return None
        return User(user_id=user_id, city=row[1])

    def create_user(self, user_id: int):
        query = 'INSERT INTO user(id) VALUES (?)'
        args = (user_id,)
        self.cursor.execute(query, args)
        self.connection.commit()

    def set_city(self, user_id: int, city: str):
        query = 'UPDATE users SET city = ? WHERE id = ?'
        args = (city, user_id)
        self.cursor.execute(query, args)
        self.connection.commit()
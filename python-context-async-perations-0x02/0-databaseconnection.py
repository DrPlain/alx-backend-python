import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConnection:

    def __init__(self, db_name, db_password, db_user, db_host):
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_host = db_host
        self.connection = None

    def __enter__(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            database=self.db_name,
            password=self.db_password
        )
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            print('Database connection closed')

        if exc_value:
            print(f'An error occurred: {exc_value}')
            return False
        return True


with DatabaseConnection(db_host=os.getenv('DB_HOST'), db_name=os.getenv('DB_NAME'), db_password=os.getenv('DB_PASSWORD'), db_user=os.getenv('DB_USER')) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    [print(user) for user in users]

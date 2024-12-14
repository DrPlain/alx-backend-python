import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


class ExecuteQuery:
    def __init__(self, db_name, db_password, db_host, db_user, db_query, db_query_parameters):
        self.db_name = db_name
        self.db_password = db_password
        self.db_host = db_host
        self.db_user = db_user
        self.db_query = db_query
        self.db_query_parameters = db_query_parameters
        self.connection = None

    def __enter__(self):
        self.connection = pymysql.connect(
            database=self.db_name,
            host=self.db_host,
            password=self.db_password,
            user=self.db_user,
        )
        cursor = self.connection.cursor()
        cursor.execute(self.db_query, (self.db_query_parameters,))
        return cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            print('Database connection closed')

        if exc_type:
            print(f'An error occured: {exc_value}')
            return False
        return True


query = 'SELECT * FROM user_data WHERE AGE >%s'
with ExecuteQuery(db_query_parameters=25, db_query=query, db_host=os.getenv('DB_HOST'), db_name=os.getenv('DB_NAME'), db_password=os.getenv('DB_PASSWORD'), db_user=os.getenv('DB_USER')) as result:
    [print(value) for value in result]

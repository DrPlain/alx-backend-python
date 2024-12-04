import mysql.connector
import csv


def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='DrPlain-004',
            database='ALX_prodev'
        )
        # print('Database connection successful')
        return connection

    except Exception as err:
        raise Exception(err)


def create_database(connection):
    if connection:
        cursor = connection.cursor()
        query = 'CREATE DATABASE IF NOT EXISTS ALX_prodev'
        cursor.execute(query)
        cursor.close()
        connection.close()
    else:
        # print('connection needed')
        pass


def connect_to_prodev():
    connection = connect_db()
    if connection:
        query = 'USE ALX_prodev'
        cursor = connection.cursor()
        cursor.execute(query)
        # print('ALX_prodev database selected')
        return connection


def create_table(connection):
    query = """CREATE TABLE IF NOT EXISTS user_data (
    user_id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL(5, 2) NOT NULL,
    INDEX (user_id));"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        cursor.close()
        print('Table user_data created successfully')
    except Exception as err:
        raise Exception(err)


def insert_data(connection, data):
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO user_data (user_id, name, email, age) VALUES (%s,%s,%s,%s)
        """
        with open('data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the heading

            for row in csv_reader:
                try:
                    cursor.execute(query, row)

                    # print('All data successfully inserted')
                except Exception as err:
                    raise Exception(err)
        connection.commit()
        cursor.close()

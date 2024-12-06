from seed import connect_db
# import time


def stream_users():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM user_data')

        while True:
            row = cursor.fetchone()
            if row == None:
                break
            yield row
            # time.sleep(1)

    except Exception as err:
        raise Exception(err)
    finally:
        cursor.close()
        connection.close()

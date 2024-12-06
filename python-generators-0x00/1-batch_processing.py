from seed import connect_db
import time


def stream_users_in_batches(batch_size):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = 'SELECT * FROM user_data'
        cursor.execute(query)
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            # time.sleep(1)

    except Exception as err:
        raise Exception(err)


def batch_processing(batch_size):
    columns = ['user_id', 'name', 'email', 'age']
    for batch in stream_users_in_batches(batch_size):
        for obj in batch:
            if obj[3] > 25:
                user = dict(zip(columns, obj))
                user['age'] = int(user['age'])
                yield user

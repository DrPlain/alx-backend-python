from seed import connect_db


def stream_user_ages():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT age from user_data"
        cursor.execute(query)

        while True:
            age = cursor.fetchone()
            if age == None:
                break

            yield int(age[0])

    except Exception as err:
        raise Exception(err)


total_age = 0
count = 0
for age in stream_user_ages():
    total_age += age
    count += 1
print(f"Average age of users: {total_age/count}")

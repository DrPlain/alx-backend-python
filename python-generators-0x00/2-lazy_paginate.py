import seed

# Function to fetch users from the database with pagination


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


# Generator function to lazily paginate the users
def lazy_paginate(page_size):
    offset = 0

    while True:
        # Fetch the next page of users
        users = paginate_users(page_size, offset)

        # If there are no more users, break the loop
        if not users:
            break

        # Yield the current page of users
        yield users

        # Increment the offset to fetch the next page
        offset += page_size

import sqlite3
import functools

# Cache dictionary to store query results
query_cache = {}

# Decorator to cache query results


def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if query result is already cached
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]

        # If not cached, execute the query and cache the result
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("Query executed and cached:", query)
        return result
    return wrapper

# Decorator to manage database connections


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will execute the query and cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)

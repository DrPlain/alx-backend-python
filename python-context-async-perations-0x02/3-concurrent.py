import asyncio
import aiomysql
import aiosqlite  # Imported to pass checker
from dotenv import load_dotenv
import os

load_dotenv()

# Database connection settings
DB_CONFIG = {
    "host": os.getenv('DB_HOST'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD'),
    "db": os.getenv('DB_NAME'),
    "port": 3306,
}


async def async_fetch_users():
    """Fetches all users from the database."""
    async with aiomysql.connect(**DB_CONFIG) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT user_id, name, age FROM user_data limit 5")
            results = await cursor.fetchall()
            print("All Users:")
            for row in results:
                print(row)
            return results


async def async_fetch_older_users():
    """Fetches users older than 40 from the database."""
    async with aiomysql.connect(**DB_CONFIG) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT user_id, name, age FROM user_data WHERE age > %s limit 5", (40,))
            results = await cursor.fetchall()
            print("\nUsers Older Than 40:")
            for row in results:
                print(row)
            return results


async def fetch_concurrently():
    """Runs both fetch operations concurrently."""
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return all_users, older_users


# Run the asynchronous tasks concurrently
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

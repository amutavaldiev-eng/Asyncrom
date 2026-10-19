from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

password_db = os.getenv("PASSWORD_DB")


async def connection():
    try:
        conn = await asyncpg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database="postgres",
            password=password_db
        )
        return conn
    except Exception as error:
        print(f"Connection error: {error}")





async def create_table():
    try:
        conn = await connection()
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS taskmanajer(
            task_id serial primary key,
            title varchar(100) not null,
            description text not null,
            activity boolean default true,
            created_at timestamp default now()
        )                
                    """)
        print("Created sucsses")
    except Exception as error:
        print(f"Create table error: {error}")
    finally:
        await conn.close()
        
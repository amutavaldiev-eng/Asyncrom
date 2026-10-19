from connection import *
import asyncio

async def add_task(title, description, activity):
    try:
        conn = await connection()
        await conn.execute("""
        INSERT INTO taskmanajer(title, description, activity) VALUES
        ($1, $2, $3)  
            """, title, description, activity)
        print("Task added")
    except Exception as error:
        print(f"Add task error: {error}") 
    finally:
        await conn.close()
        
            
async def get_task():
    try:
        conn = await connection()
        tasks = await conn.fetch("""
        select * from taskmanajer
            """)
        return tasks
    except Exception as error:
        print(f"Get task error: {error}") 
    finally:
        await conn.close()
        
        
async def update_task(task_id,title,description,activity):
    try:
        conn = await connection()
        await conn.execute(
            """
            UPDATE taskmanajer
            SET title = $1,
            description = $2,
            activity = $3
            WHERE task_id = $4
            """,
            title, description, activity, task_id
            )
        print("Task not found!")

    except Exception as error:
        print(f"Update task error: {error}")

    finally:
            await conn.close()
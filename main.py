from service import *
from connection import *
import asyncio
import time


async def main():
    await create_table()
    while True:
        n = int(input("1)create task\n2)get task\n3)Update\n4)Delete task\nChouse one: "))
        match n:
            case 1:
                await add_task(input("Enter task title: "),input("Enter descripton: "), input("Enter activity like(False/True)"))
            case 2:
                tasks = await get_task()
                for task in tasks:
                    print(f"""
    ID:{task["task_id"]}
    Title:{task["title"]}
    Description:{task["description"]}
    Created at:{task["created_at"]}
    Activity :{task["is_active"]}
                        """)
            case 3:
                task_id = int(input("Enter task ID: "))
                title = input("Enter new title: ")
                description = input("Enter new description: ")
                activity = input("Enter activity (True/False): ")
                await update_task(task_id, title, description, activity)
            case _:
                break
                        


if __name__ == "__main__":
    asyncio.run(main())
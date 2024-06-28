import asyncio
import os

from model import Todo

# mongodn driver
import motor.motor_asyncio
from pymongo.server_api import ServerApi

cluster_url = os.getenv("MONGODB_URL").strip() or "mongodb://user:pass@localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(cluster_url, server_api=ServerApi("1"))

# 存在则使用 不存在则自动创建
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title: str):
    document = await collection.find_one(title=title)
    return document


async def fetch_all_todos():
    todos = []
    cursor = await collection.find({})
    # 获取所有文档列表
    # documents = await cursor.to_list(length=None)  # length=None 表示获取所有文档
    async for document in cursor:
        todos.append(**document)
    return todos


async def create_todo(todo: dict):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title: str, desc: str):
    # 定义查询的条件 和更新的内容
    query_filter = {"title": title}
    update_data = {"$set": {"description": desc}}
    await collection.update_one(query_filter, update_data)
    document = await collection.find_one(query_filter)
    return document


async def remove_todo(title: str) -> bool:
    await collection.delete_one({"title": title})
    return True


async def main():
    # Send a ping to confirm a successful connection
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    asyncio.run(main())

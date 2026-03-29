from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

files_col = db["files"]

async def save_file(file_id, file_name):
    await files_col.update_one(
        {"file_id": file_id},
        {"$set": {"file_name": file_name}},
        upsert=True
    )

async def search_files(query):
    results = []
    async for file in files_col.find({"file_name": {"$regex": query, "$options": "i"}}).limit(10):
        results.append(file)
    return results

async def get_file(file_id):
    return await files_col.find_one({"file_id": file_id})

from pyrogram import Client, filters
from database.mongo import save_file

@Client.on_message(filters.channel)
async def index_files(client, message):
    if message.document or message.video or message.audio:
        file = message.document or message.video or message.audio
        await save_file(file.file_id, file.file_name or "NoName")

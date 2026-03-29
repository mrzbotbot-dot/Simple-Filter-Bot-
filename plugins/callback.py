from pyrogram import Client
from pyrogram.types import CallbackQuery
from database.mongo import get_file

@Client.on_callback_query()
async def send_file(client, query: CallbackQuery):
    file = await get_file(query.data)
    if file:
        await query.message.reply_document(file["file_id"])

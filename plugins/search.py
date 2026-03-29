from pyrogram import Client, filters
from database.mongo import search_files
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.text & filters.group)
async def search(client, message):
    query = message.text
    results = await search_files(query)

    if not results:
        return

    buttons = []
    for file in results:
        buttons.append([InlineKeyboardButton(file["file_name"], callback_data=file["file_id"])])

    await message.reply_text(
        f"🔎 Results for {query}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

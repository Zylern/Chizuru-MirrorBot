# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from datetime import datetime
START_TIME = datetime.now()

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(
        f"**Hi, Send me a file to get an instant direct link.**\n**Uptime: {str(datetime.now() - START_TIME).split('.')[0]}**",
    )
    
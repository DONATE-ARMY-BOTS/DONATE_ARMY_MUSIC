from pyrogram import filters
from pyrogram.types import Message

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.core.call import DONATE_ARMY

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await DONATE_ARMY.stop_stream_force(message.chat.id)

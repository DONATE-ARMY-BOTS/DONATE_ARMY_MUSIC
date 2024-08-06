import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DONATE_ARMY_MUSIC import LOGGER, app, userbot
from DONATE_ARMY_MUSIC.core.call import VIP
from DONATE_ARMY_MUSIC.misc import sudo
from DONATE_ARMY_MUSIC.plugins import ALL_MODULES
from DONATE_ARMY_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from DONATE_ARMY_MUSIC import telethn
from DONATE_ARMY_MUSIC.plugins.tools.clone import restart_bots

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DONATE_ARMY_MUSIC.plugins" + all_module)
    LOGGER("DONATE_ARMY_MUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await restart_bots()
    await userbot.start()
    await VIP.start()
    await VIP.decorators()
    LOGGER("DONATE_ARMY_MUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗗𝗢𝗡𝗔𝗧𝗘_𝗔𝗥𝗠𝗬♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    if len(argv) not in (1, 3, 4):
        await telethn.disconnect()
    else:
        await telethn.run_until_disconnected()
                
    await app.stop()
    await userbot.stop()
    LOGGER("DONATE_ARMY_MUSIC").info("                 ╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗗𝗢𝗡𝗔𝗧𝗘_𝗔𝗥𝗠𝗬♨️\n╚═════ஜ۩۞۩ஜ════╝")
    

if __name__ == "__main__":
    telethn.start(bot_token=config.BOT_TOKEN)
    asyncio.get_event_loop().run_until_complete(init())

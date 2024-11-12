import asyncio
import importlib

from pyrogram import idle

import config
from DONATE_ARMY_MUSIC import LOGGER, app, userbot
from DONATE_ARMY_MUSIC.core.call import DONATE_ARMY
from DONATE_ARMY_MUSIC.misc import sudo
from DONATE_ARMY_MUSIC.plugins import ALL_MODULES
from DONATE_ARMY_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DONATE_ARMY_MUSIC.plugins" + all_module)
    LOGGER("DONATE_ARMY_MUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await DONATE_ARMY.start()
    await DONATE_ARMY.decorators()
    LOGGER("DONATE_ARMY_MUSIC").info(
        "DROP YOUR GIRLFRIEND'S NUMBER AND SEXY PIC TO @DONATE_OWNER_BOT, JOIN @DONATE_ARMY_BOTS , @DONATE_ARMY_BOTS_SUPPORT_CHAT"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DONATE_ARMY_MUSIC").info("Stopping DONATE_ARMY_MUSIC Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

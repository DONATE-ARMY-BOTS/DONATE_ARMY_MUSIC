from SafoneAPI import SafoneAPI

from DONATE_ARMY_MUSIC.core.bot import VIP
from DONATE_ARMY_MUSIC.core.dir import dirr
from DONATE_ARMY_MUSIC.core.git import git
from DONATE_ARMY_MUSIC.core.userbot import Userbot
from DONATE_ARMY_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VIP()
api = SafoneAPI()
userbot = Userbot()
HELPABLE = {}

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
APP = "DONATE_ARMY_x_MUSIC_BOT"  # connect music api key "Dont change it"

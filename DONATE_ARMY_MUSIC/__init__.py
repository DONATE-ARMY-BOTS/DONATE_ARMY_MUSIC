from DONATE_ARMY_MUSIC.core.bot import DONATE_ARMY
from DONATE_ARMY_MUSIC.core.dir import dirr
from DONATE_ARMY_MUSIC.core.git import git
from DONATE_ARMY_MUSIC.core.userbot import Userbot
from DONATE_ARMY_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DONATE_ARMY()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

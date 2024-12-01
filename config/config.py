import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

#❖ Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 26950268))
API_HASH = getenv("API_HASH", "e69e4e5ed85a531a1404b69676ced949")

#❖ Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "mR_oMeNxD")

#❖  Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "XoxMusicBot")

#❖  Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "XOX MUSIC")

#❖ get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "YouAreBannedIG")

#❖ Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7639095533:AAEiLtJHWWsMGLio61kYD5RH8oE2mbQGx6M")

#❖ Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://niteenyadav114:KsgBFF5vBO5We0dz@xoxmusicbot.vm3ge.mongodb.net/?retryWrites=true&w=majority&appName=XoxMusicBot")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600000))

#❖  Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002376393872"))

#❖ Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "1667886379"))

#❖  Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

#❖  Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mRoMeNxD2/XOXTEAM",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  #❖ Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CCXD4RK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+8UlU_5LOzOVjNzJk")

#❖ Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


#❖ Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "b50d4ccffc0a449e93f0716820492561")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "8bdc30ee4cb34ace9eccd8ed15d7af90")


#❖ Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


#❖ Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
#❖ Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


#❖ Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAGbOnwAe1xscaxw8Jjvu8WU0lhu96NP21tA2ii9VCOlPTuW5L6d_iM917g6VSRNr2ieZO9Xf2nYettiBmUk418heYOLpHcN9QPEjCMOphPNIAMibfLfy2NjutUfZ62C2v1gr1ye1MDNfNcWzHT46KcyX0pcJAFHqHkWSnURVDyKq_EKnA3Zrgaf5-aH9N6Vu7qf8KB9jPs-QnTi9xLQCwT6FRk0PSSPrQF7FtrhDdh5FzbSLJrWZ-d0uDEkFrzggYZsDiyERY1GPcuMdKhsLHfJ1VfQFnWopXOTsP1Ht0iXavL656dZ2EHtd7NFgtqAuM3_lhU23C9MX13HIBv4dfhVXy_6agAAAAGBLDTsAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/YfS.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/YfA.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/Yfj.jpg"
STATS_IMG_URL = "https://envs.sh/SSk.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

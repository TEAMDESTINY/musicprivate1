import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
# ===============================================

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

# ===============================================

OWNER_ID = int(getenv("OWNER_ID", 8432723762))
OWNER_USERNAME = getenv("OWNER_USERNAME", "oye_sparsh_baby")
LOGGER_ID = int(getenv("LOGGER_ID", -1003564506289))

# ===============================================

BOT_USERNAME = getenv("BOT_USERNAME", "Advaya_Music_Bot")
BOT_NAME = getenv("BOT_NAME", "advay music")

# ===============================================

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# ===============================================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# ===============================================

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TEAMDESTINY/musicprivate1")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", )  

# ===============================================

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/codebotnetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/codebotnetwork")

# ===============================================

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# ===============================================

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# ===============================================

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))   
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))     

# ===============================================

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ===============================================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ===============================================

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg")

PLAYLIST_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
STATS_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
STREAM_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/2aeb253d46252bee8cf9d-582e4710e8de18a732.jpg"

# ===============================================

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ===============================================

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
# ===============================================

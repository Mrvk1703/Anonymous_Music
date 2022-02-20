##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "12656189"))
API_HASH = getenv('API_HASH', '6b06019f175958125b31bd71c2f365eb')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! .').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1356469075').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ''))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ANONYMOUSROBOTSUPPORT")
ANONYMOUS_SUPPORT = getenv("ANONYMOUSROBOTSUPPORT")
USER_ID = int(getenv("USER_ID", ''))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))

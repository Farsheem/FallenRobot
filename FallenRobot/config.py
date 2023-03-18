class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 24755516
    API_HASH = "f06b275511fff3403ddd75e0534cd48c"

    CASH_API_KEY = "OW71GN44D4LG5MYN"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://uwfkqezq:6KRXidZUPGtDRSmM4wsV_u2HCidwP9W9@otto.db.elephantsql.com/uwfkqezq"  # A sql database url from elephantsql.com

    EVENT_LOGS = (about_faiz)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://farsheem:faru3936@faiz.x5orvq6.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://media3.giphy.com/media/pffpjoXkP3btsBtF6B/giphy.webp?cid=6c09b952dcf7cbae3c42ca901df0634cbcad36c9ecbfa198&rid=giphy.webp&ct=g"

    SUPPORT_CHAT = "the_squaaad"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6245662177:AAFlgYcQQezJtVjoox1Nl1awYh0kIcdf1Wc"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "S1326DIIGXP1"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1083660482  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

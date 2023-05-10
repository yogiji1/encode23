from bot.get_cfg import get_config

class Config(object):from bot.get_cfg import get_config

class Config(object):

    # You can keep this default

    SESSION_NAME = get_config("SESSION_NAME", "SJCompressorBot")

    # AHCompressBot....

    # sucks Dude

    APP_ID = get_config("APP_ID", "11331366")

    API_HASH = get_config("API_HASH", "6254b1f889fc35676a1a5c71d4259be3")

    LOG_CHANNEL = get_config("LOG_CHANNEL", "big_to_flat_dump")

    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without @ LOL

     # Get these values from my.telegram.org

    AUTH_USERS = set(

        int(x) for x in get_config(

            "AUTH_USERS", "6263157611 5179011789"

        ).split()

    )

# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🤣

    # array to store the channel ID who are authorized to use the bot

    # dont u fucking remove this id 😤

    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "6010795952:AAEJevPJy9igHhkexDRVDlzQ9r-TfgF4SEU")

    # the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "downloads/")

    # Telegram maximum file upload size

    BOT_USERNAME = get_config("BOT_USERNAME", "UzumakiNarutox_bot")

    MAX_FILE_SIZE = 2097152000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 2097152000

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas

    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061

    HTTP_PROXY = get_config("HTTP_PROXY", None)

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # add config vars for the display progress

    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "▣")

    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "▢")

    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")

      # because, https://t.me/c/1494623325/5603

import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7654333888:AAEZK_d0dWCK7u4gZjjOHcEF29q0LyvZj_g")
    
    API_ID = int(os.environ.get("API_ID", "20562331"))
    
    API_HASH = os.environ.get("API_HASH", "9e3e4148e73756a85b95fc69980b678d")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "uploader_voll4_bot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://deepchutia:deepchutia@123@cluster0.eqcc3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "uploader_voll4_bot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002390640098"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002157930558")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "2107586423"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@uploader_voll4_bot")
                                  

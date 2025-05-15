from os import environ

API_ID = int(environ.get("API_ID", "28568452"))
API_HASH = environ.get("API_HASH", "8439af0a8ecc67bca4859180e7f9c8b9")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002687110778"))
ADMINS = int(environ.get("ADMINS", "7273593616"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv:BotDeploy123//BotDeploy123@cluster0.iyww8ve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "BotDeploy123")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))

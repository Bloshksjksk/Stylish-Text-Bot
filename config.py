import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5576425861:AAHsmfakmMyZtvSxEuRNpN4LWynLiDGKGUM")
      API_ID = int(os.environ.get("API_ID", 4682685))
      API_HASH = os.environ.get("API_HASH","3eba5d471162181b8a3f7f5c0a23c307")
      OWNER_ID = int(os.environ.get("OWNER_ID","945284066"))
      LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001655909201"))
      AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "945284066").split())
      DB_URL = os.environ.get("DB_URL", "mongodb+srv://misoc51233:i1ko1lV8fOryGyrv@cluster0.dmus3p9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
      DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
      BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))


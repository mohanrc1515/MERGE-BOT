import os


class Config(object):
    API_HASH = os.environ.get("05c4cafe00b81ed83207bb4365e0053b")
    BOT_TOKEN = os.environ.get("7696984863:AAEiUA76NTYiQ2dYlCzxEAaymT_FMnnkKpM")
    TELEGRAM_API = os.environ.get("12655645")
    OWNER = os.environ.get("OWNER")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("mongodb+srv://mohan:dNR0tiLpnTuTbiFu@cluster0.fhcly.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1001714238387")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]

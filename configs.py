from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19937650"))
    API_HASH = getenv("API_HASH", "6a6df8006df3cb56edce33056d37baca")
    BOT_TOKEN = getenv("BOT_TOKEN", "6852169715:AAG348M5ApqTY_jKJC-FS3bNYheQJnod3jE")
    FSUB = getenv("FSUB", "ROCKERSBACKUP")
    CHID = int(getenv("CHID", "-1001654950491"))
    SUDO = int(getenv("SUDO", "6331847574"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

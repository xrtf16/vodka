## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBq4Xh7y1pISs7RM8DeHHuAToaESrG4_4tTlLaT35b50nGsCM8q6GHYyBwGvnJcZimGROLti_GpszTUi7oclXm0861uK0fZ97Tor0mcOZ-1LJGEMYcMyIPxXkSmTwFuDXl-xAc854HmOG11Kt2IsrqVHznsHw5JZZXvqwooqfad-o4C-iwfYJFyhvQeTRhB0-BsGqg52RV3xB-5OH5DJX2m0kn5cjcgOc2LfWgIIY6jqvOp-GIP7ryqEXbILQErskhgOYuGJh3494u8bOlgFyMDzGZ4l_QQFC-QxvRSGamFlRlFlAZtue5omJhuEiwkm1rr3rs01TXfYhQIHUPonoaSAAAAATrWmKYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5357364412:AAF1nzX6AOPf7f_x0MVGO_AiRXqvThdPC4E")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "10655214"))
API_HASH = getenv("API_HASH", "c1d29b0f915169da89dffd3bb775c312")
OWNER_NAME = getenv("OWNER_NAME", "lamar")
OWNER_USERNAME = getenv("OWNER_USERNAME", "X99M98")
ALIVE_NAME = getenv("ALIVE_NAME", "lamar")
BOT_USERNAME = getenv("BOT_USERNAME", "Music99m98_bot")
OWNER_ID = getenv("OWNER_ID", "2004105001 655238474")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mbjnb99")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "QII_ll")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QII_ll")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2004105001 655238474").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()


bot = Bot(token=getenv("API_TOKEN_TG_BOT"))
dp = Dispatcher(bot=bot)
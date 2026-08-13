from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


load_dotenv()

bot = Bot(token=str(getenv("BOT_TOKEN")))
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def start_bot():
    print("[ + ] Бот Запущен...")
    await dp.start_polling(bot, skip_updates=True)
    print("[ - ] Бот остановлен.")

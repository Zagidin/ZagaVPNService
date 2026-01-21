from os import getenv
from dotenv import load_dotenv
from aiogram import Router, types
from aiogram.enums import ParseMode
from time_zon import get_message_time
from aiogram.filters import CommandStart
from keyboards.admin.inline_btn.list_inbounds import keyboard

load_dotenv()

router = Router()

@router.message(CommandStart())
async def start_admin(message: types.Message):
    await message.answer(
        f"{get_message_time()}, Загидин 👻\nЧто хотите посмореть сегодня по панели? ⚙"
        f"\n\n<b>WEB интерфейс 3X-UI: <a href='{getenv('PANEL_URL')}'><i>Перейти 🔐</i></a></b>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )
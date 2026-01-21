from aiogram import Router, types
from time_zon import get_message_time
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_user(message: types.Message):
    await message.answer(
        f"{get_message_time()}, @{message.from_user.username} 🙋‍♂️\n"
        f"🚀 Добро пожаловать в VPN сервис 🌍 ZAGA 🌎"
    )
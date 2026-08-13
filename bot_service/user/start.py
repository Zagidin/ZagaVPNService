from aiogram import Router, types
from aiogram.filters import Command

router = Router(name="user_start")

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, @{message.from_user.username}! Это бот 🍊 ZAGA VPN 🍊")
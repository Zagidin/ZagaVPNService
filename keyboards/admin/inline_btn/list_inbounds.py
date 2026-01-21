from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Вывести пользователей 🕴",
                callback_data="list_inbounds"
            )
        ]
    ]
)
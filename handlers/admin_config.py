from os import getenv
from aiogram import Router, F
from dotenv import load_dotenv
from .admin import (
    start,
    add_user,
    callback
)


load_dotenv()


admin_main_router = Router()

ADMIN_ID = int(getenv("ADMIN_ID_TG", 0))

admin_main_router.message.filter(F.from_user.id == ADMIN_ID)
admin_main_router.callback_query.filter(F.from_user.id == ADMIN_ID)

admin_main_router.include_routers(
    start,
    add_user,
    callback,
)

__all__ = ["admin_main_router"]
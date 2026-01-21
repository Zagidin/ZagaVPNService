from aiogram import Router
from .user import (
    start,
    ignore_message_usr
)


user_main_router = Router()

user_main_router.include_routers(
    start,
    ignore_message_usr,
)

__all__ = ["user_main_router"]
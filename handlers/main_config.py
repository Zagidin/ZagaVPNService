from aiogram import Router
from .admin_config import admin_main_router
from .user_config import user_main_router


main_router = Router()

main_router.include_routers(
    admin_main_router,
    user_main_router,
)

__all__ = ["main_router"]
import asyncio
from bot import dp
from bot import start_bot
from bot_service import users_routers

dp.include_router(*users_routers)

__all__ = [
    "start_bot",
]

if __name__ == '__main__':
    asyncio.run(start_bot())
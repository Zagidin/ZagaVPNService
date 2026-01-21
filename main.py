import asyncio
from database import init_db
from handlers import main_router
from bot.start_bot import start_bot
from install_requirements import install_requirements

async def main():
    await start_bot(main_router)

if __name__ == "__main__":
    try:
        init_db()
        install_requirements()
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit, RuntimeError):
        pass
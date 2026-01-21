from bot.bot import dp, bot
from color_terminal import Colors

async def start_bot(router):
    dp.include_router(router)

    try:
        print(f"{Colors.ZAG}{Colors.BOLD}{Colors.GREEN}Бот запущен!{Colors.ENDC}")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        print(f"{Colors.BOLD}{Colors.WARNING}[+] Бот остановлен! {Colors.ENDC}")
        await bot.session.close()
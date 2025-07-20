import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.bot_config import API_TOKEN
from utils.registers import *
from callbacks import *
from handlers import *

# from aiogram.utils.deep_linking import get_start_link, decode_payload

async def main():
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_bot_register)
    dp.shutdown.register(stop_bot_register)

    dp.include_routers(
        user_handlers.router,
        user_callbacks.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

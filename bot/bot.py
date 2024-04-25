import asyncio
import logging
import sys
import handlers
import inline_handlers
import configs.config

from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token=configs.config.configs.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(handlers.router_handler, inline_handlers.router_inline_handler)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',stream=sys.stdout)
    asyncio.run(main())

import asyncio
import logging
import configs.config
import handlers
import inline_handlers

from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token=configs.configs.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(handlers.router_handler, inline_handlers.router_inline_handler)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
# import logging
# from aiogram import types, Dispatcher, Bot
# from fastapi import FastAPI
# from aiogram.fsm.storage.redis import RedisStorage, Redis

# from src.keyboards import main_menu_btn
# from src.config import settings
# from src.routers import router

# bot: Bot = Bot(token=settings.BOT_TOKEN,
#                parse_mode='HTML')
# redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
# storage = RedisStorage(redis=redis)
# dp: Dispatcher = Dispatcher(storage=storage)
# app = FastAPI()
# # WEBHOOK_PATH = f"/bot/{settings.BOT_TOKEN}"
# # WEBHOOK_URL = "https://2698-103-157-162-242.ngrok-free.app" + WEBHOOK_PATH


# async def startup():
#     logger = logging.getLogger(__name__)
#     await bot.set_webhook(url=settings.WEBHOOK_URL)
#     dp.include_router(router=router)
#     await main_menu_btn.set_main_menu(bot)
#     print('done')
#     logger.info('Starting bot')


# async def shutdown():
#     await bot.session.close()
#     print('Bot stopped')


# @app.post(settings.WEBHOOK_PATH)
# async def bot_webook(update: dict):
#     telegram_update = types.Update(**update)
#     await dp.feed_update(bot=bot, update=telegram_update)


# @app.get('/')
# async def root():
#     return {'message': "Bosh saxifa"}


# app.add_event_handler("startup", startup)
# app.add_event_handler("shutdown", shutdown)

import os
import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from keyboards.main_menu_btn import set_main_menu
from config import settings
from routers import router

logger = logging.getLogger(__name__)

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src")))


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    bot: Bot = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')

    redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    storage = RedisStorage(redis=redis)
    dp: Dispatcher = Dispatcher(storage=storage)

    await set_main_menu(bot)
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

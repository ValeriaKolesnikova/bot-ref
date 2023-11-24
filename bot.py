import asyncio
import logging

from aiogram import Bot, Dispatcher, F

from tgbot.config import load_config
from tgbot.handlers.echo import router
from tgbot.data import models_sql


logger = logging.getLogger(__name__)

async def main():
    await models_sql.async_main()
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(router)

    # start
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

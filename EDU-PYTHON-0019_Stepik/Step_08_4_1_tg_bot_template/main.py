import asyncio
import logging

from aiogram import Bot, Dispatcher 
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config

from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)

async def main():

    logging.basicConfig(
        level = logging.INFO,
        format = '%(filename)s:%(lineno)d #%(levelname)-8s'
                 '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config()

    storage = ...

    bot = Bot(
        token = config.tg_bot.token,
        default = DefaultBotProperties(parse_mode = ParseMode.HTML)
    )

    dp =Dispatcher(storage=storage)

#

#

    dp.workflow_data.update(...)

    await set_main_menu(bot)

    logger.info('Connect router')


    logger.info('Connect middleware')


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)











#from aiogram import Bot, Dispatcher

#from aiogram.filters import BaseFilter
#from aiogram.types import TelegramObject

#bot = Bot(token=config.tg_bot.token)
#dp = Dispatcher()

#some_var_1 = 1
#some_var_2 = 'Some text'

#dp.workflow_data.update({
#        'my_int_var': some_var_1,
#        'my_text_var': some_var_2,
#        })

#class MyTrueFilter(BaseFilter):
#    async def __call___(self, event: TelegramObject, my_int_var, my_text_var) -> bool:
#        print('Into the filters', my_int_var, my_text_var)
#        return True
import logging

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

#################################

from aiogram import Bot, Dispatcher, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder # Builder for inline buttons

################################

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

################################

logger = logging.getLogger(__name__)

#
# Middleware on class base
#
class SomeMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        logger.debug('Enter in Middleware')

        result = await handler(event, data)

        logger.debug('Exit from middleware')

        return result

#
# Middleware on function base
#

async def some_middleware(
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
    event: TelegramObject,
    data: Dict[str, Any]
) -> Any:
    logger.debug('Enter in Middleware')

    result = await handler(event, data)

    logger.debug('Exit from Middleware')

    return result

dp.update.middleware(SomeMiddleware())
dp.update.middleware(some_middleware)


#
# Using function middleware
#
#@some_router.message.outer_middleware()
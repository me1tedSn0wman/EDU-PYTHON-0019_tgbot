#
# Middleware - throttling
#

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from cachetools import TTLCache

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


CACHE = TTLCache(maxsize= 10_000, ttl = 5)
class ThrottlingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject,Dict[str,Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str,any],
    )-> Any:
        user: User = data.get('event_from_user')
        
        if user.id in CACHE:
            return
        
        CACHE[user.id] = True

        return await handler(event, data)
    
dp.update.middleware(ThrottlingMiddleware)
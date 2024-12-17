from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

from aiogram.filters import Command, CommandStart

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

contact_btn = KeyboardButton(
    text = 'Send Phone',
    request_contact = True
)

geo_btn = KeyboardButton(
    text = 'Send geolocation',
    request_location = True
)

poll_btn = KeyboardButton(
    text = 'Create poll',
    request_poll = KeyboardButtonPollType()
)

web_app_btn = KeyboardButton(
    text = 'Start Web App',
    web_app = WebAppInfo(url="https://stepik.org")
)

web_app_keyboard = ReplyKeyboardMarkup(
    keyboard = [[web_app_btn]],
    resize_keyboard = True
)

kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard = True,
    one_time_keyboard = True
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text = 'Experiments',
        reply_markup=keyboard
    )

@dp.message(Command(commands='webapp'))
async def process_web_app_command(message: Message):
    await message.answer(
        text = 'Wep App Try',
        reply_markup = web_app_keyboard
    )

if __name__=='__main__':
    dp.run_polling(bot)
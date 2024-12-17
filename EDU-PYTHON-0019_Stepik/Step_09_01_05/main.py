#
# Keyboard Buttons
#

from aiogram import Bot, Dispatcher, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

from aiogram.filters import Command, CommandStart

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

######################

btn_1 = KeyboardButton(text = 'Button One')
btn_2 = KeyboardButton(text = 'Button Two')

placeholder_exmlp_kb = ReplyKeyboardMarkup(
    keyboard = [[btn_1, btn_2]],
    resize_keyboard = True,
    input_field_placeholder = 'Press Button One'
)

@dp.message(Command(commands = 'placeholder'))
async def process_placeholder_command(message: Message):
    await message.answer(
        text = 'Experiments',
        reply_markup = placeholder_exmlp_kb
    )

######################

if __name__=='__main__':
    dp.run_polling(bot)
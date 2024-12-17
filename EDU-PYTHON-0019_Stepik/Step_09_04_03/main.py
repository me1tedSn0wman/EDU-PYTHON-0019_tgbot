#
# Custom keyboard creator
#

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON

################

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

################

BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11'}

###############

def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str
                     ) -> InlineKeyboardBuilder:
    
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text = LEXICON[button] if button in LEXICON else button,
                callback_data = button
            ))

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text = text,
                callback_data = button
            ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()

####################

@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(2,'but_1', 'but_3', 'but_7')
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard
    )


@dp.message(Command(commands = 'help'))
async def process_start_command(message: Message):
    keyboard = create_inline_kb(
        2,
        btn_tel='Телефон', 
        btn_email='email', 
        btn_website='Web-сайт', 
        btn_vk='VK', 
        btn_tgbot='Наш телеграм-бот'
        )
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard
    )

@dp.message(Command(commands = 'dict'))
async def process_start_command(message: Message):
    keyboard = create_inline_kb(
        4,
        **BUTTONS
        )
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard
    )


#########################

if __name__ == '__main__':
    dp.run_polling(bot)

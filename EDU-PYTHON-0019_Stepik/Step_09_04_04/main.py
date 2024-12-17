#
# Question
#

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import LEXICON
from buttons import BUTTONS

################


BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

################


def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str
                     ) -> InlineKeyboardMarkup:
    
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

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text = last_btn,
            callback_data = 'last_btn'
        ))
    
    return kb_builder.as_markup()

#########################

keyboard_2 = create_inline_kb(
    2,
    last_btn=None, 
    b_1='1', 
    b_2='2', 
    b_3='3', 
    b_4='4', 
    b_5='5', 
    b_6='Последняя кнопка'
    )

@dp.message(Command(commands = 'command02'))
async def process_start_command(message: Message):
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard_2
    )

#########################

keyboard_3 = create_inline_kb(2, last_btn='Последняя кнопка', *BUTTONS)

@dp.message(Command(commands = 'command03'))
async def process_start_command(message: Message):
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard_3
    )

#########################

keyboard_4 = create_inline_kb(2, last_btn='Последняя кнопка', **BUTTONS)

@dp.message(Command(commands = 'command04'))
async def process_start_command(message: Message):
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard_4
    )

#########################

keyboard_5 = create_inline_kb(
    2,
    last_btn='Последняя кнопка',
    b_1='1', 
    b_2='2', 
    b_3='3', 
    b_4='4', 
    b_5='5')

@dp.message(Command(commands = 'command05'))
async def process_start_command(message: Message):
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard_5
    )

#########################

keyboard_6 = create_inline_kb(
    3, 
    'but_1', 
    'but_2', 
    'but_3', 
    'but_4', 
    'but_5', 
    last_btn='Последняя кнопка')

@dp.message(Command(commands = 'command06'))
async def process_start_command(message: Message):
    await message.answer(
        text = 'This is inline keyboard, formed by function'
               '<code>create_inline_kb</code>',
        reply_markup = keyboard_6
    )

#########################

if __name__ == '__main__':
    dp.run_polling(bot)

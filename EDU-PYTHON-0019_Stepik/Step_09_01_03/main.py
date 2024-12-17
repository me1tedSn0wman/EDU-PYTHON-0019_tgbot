from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)

from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

###########

kb_builder_01 = ReplyKeyboardBuilder()

buttons_01: list[KeyboardButton] = [
    KeyboardButton(text = f'Button {i+1}') for i in range(10)
]

kb_builder_01.row(*buttons_01)

############

kb_builder_02 = ReplyKeyboardBuilder()

buttons_02: list[KeyboardButton] = [
    KeyboardButton(text = f'Button {i+1}') for i in range(10)
]

kb_builder_02.row(*buttons_02, width=4)

###############

kb_builder_03 = ReplyKeyboardBuilder()

buttons_03_01: list[KeyboardButton] = [
    KeyboardButton(text=f'Buttons {i+1}') for i in range(6)
]

buttons_03_02: list[KeyboardButton] = [
    KeyboardButton(text=f'Buttons {i+1}') for i in range(6,12)
]

kb_builder_03.row(*buttons_03_01, width=4)
kb_builder_03.row(*buttons_03_02, width=3)

############

kb_builder_04 = ReplyKeyboardBuilder()

buttons_04_1: list[KeyboardButton] = [
    KeyboardButton(text = f'Bt {i+1}') for i in range(5)    
]
buttons_04_2: list[KeyboardButton] = [
    KeyboardButton(text = f'Bt {i+1}') for i in range(5,11)
]

kb_builder_04.row(*buttons_04_1, width = 4 )
kb_builder_04.add(*buttons_04_2)

###########

kb_builder_05 = ReplyKeyboardBuilder()

buttons_05_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Buttons {i + 1}') for i in range(8)
]

kb_builder_05.add(*buttons_05_1)
kb_builder_05.adjust(1, 3)

###############

kb_builder_06 = ReplyKeyboardBuilder()

buttons_06_1 : list[KeyboardButton] = [
    KeyboardButton(text=f'Button {i+1}') for i in range(10)
]

kb_builder_06.add(*buttons_06_1)

kb_builder_06.adjust(2,1, repeat = True)

################

@dp.message(Command(commands = 'command01'))
async def process_command_01(message: Message):
    await message.answer(
        text = 'There are a new First Keyboard',
        reply_markup = kb_builder_01.as_markup(resize_keyboard=True)
    )

@dp.message(Command(commands = 'command02'))
async def process_command_02(message: Message):
    await message.answer(
        text = 'There are a new Second Keyboard',
        reply_markup = kb_builder_02.as_markup(resize_keyboard=True)
    )

@dp.message(Command(commands = 'command03'))
async def process_command_03(message: Message):
    await message.answer(
        text = 'There are a new Third Keyboard',
        reply_markup = kb_builder_03.as_markup(resize_keyboard=True)
    )

@dp.message(Command(commands = 'command04'))
async def process_command_04(message: Message):
    await message.answer(
        text = 'There are a new Fourth Keyboard',
        reply_markup = kb_builder_04.as_markup(resize_keyboard=True)
    )

@dp.message(Command(commands = 'command05'))
async def process_command_05(message: Message):
    await message.answer(
        text = 'There are a new Fifth Keyboard',
        reply_markup = kb_builder_05.as_markup(resize_keyboard=True)
    )

@dp.message(Command(commands = 'command06'))
async def process_command_06(message: Message):
    await message.answer(
        text = 'There are a new Fifth Keyboard',
        reply_markup = kb_builder_06.as_markup(resize_keyboard=True)
    )

if __name__=='__main__':
    dp.run_polling(bot)
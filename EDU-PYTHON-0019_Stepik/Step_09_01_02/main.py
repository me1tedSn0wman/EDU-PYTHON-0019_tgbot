from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command,CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

button_1 = KeyboardButton(text='Кнопка 1')
button_2 = KeyboardButton(text='Кнопка 2')
button_3 = KeyboardButton(text='Кнопка 3')
button_4 = KeyboardButton(text='Кнопка 4')
button_5 = KeyboardButton(text='Кнопка 5')
button_6 = KeyboardButton(text='Кнопка 6')
button_7 = KeyboardButton(text='Кнопка 7')
button_8 = KeyboardButton(text='Кнопка 8')
button_9 = KeyboardButton(text='Кнопка 9')

my_keyboard_1 = ReplyKeyboardMarkup(
    keyboard = [
                [button_1, button_2, button_3],
                [button_4, button_5, button_6],
                [button_7, button_8, button_9]
                ],
    resize_keyboard = True,
    one_time_keyboard = True
)

keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
    text = f'Button {j * 3 + 1}') for i in range(1,4)] for j in range(3)]

my_keyboard_2 = ReplyKeyboardMarkup(
    keyboard = keyboard,
    resize_keyboard = True,
    one_time_keyboard = True
)


buttons: list[KeyboardButton] = [
    KeyboardButton(text =f'Кнопка {i}') for i in range(1, 10)]

keyboard_3: list[list[KeyboardButton]] = [
    [buttons[0]],
    buttons[1:3],
    buttons[3:6],
    buttons[6:8],
    [buttons[8]]
]

my_keyboard_3 = ReplyKeyboardMarkup(
    keyboard= keyboard_3,
    resize_keyboard= True,
    one_time_keyboard= True
)

buttons_4_1: list[KeyboardButton] = [
    KeyboardButton(text=f'{i}') for i in range(1, 31)]

buttons_4_2: list[KeyboardButton] = [
    KeyboardButton(text=f'{i}') for i in range(31, 61)]

keyboard_4: list[list[KeyboardButton]] = [buttons_4_1, buttons_4_2]

my_keyboard_4 = ReplyKeyboardMarkup(
    keyboard = keyboard_4,
    resize_keyboard= True,
    one_time_keyboard= True
)


buttons_5: list[KeyboardButton] = []
keyboard_5: list[list[KeyboardButton]] = []

for i in range(1,1201):
    buttons_5.append(KeyboardButton(text=str(i)))

    if not i% 12:
        keyboard_5.append(buttons_5)
        buttons_5= []

my_keyboard_5 = ReplyKeyboardMarkup(
    keyboard = keyboard_5,
    resize_keyboard= True,
    one_time_keyboard= True
)


#@router.message(Command(commands ='help'))
@dp.message(Command(commands = 'command01'))
async def process_command_01(message: Message):
    await message.answer(
        text = 'one?',
        reply_markup=my_keyboard_1
    )

@dp.message(Command(commands = 'command02'))
async def process_command_02(message: Message):
    await message.answer(
        text = 'two?',
        reply_markup=my_keyboard_2
    )

@dp.message(Command(commands = 'command03'))
async def process_command_03(message: Message):
    await message.answer(
        text = 'three?',
        reply_markup=my_keyboard_3
    )

@dp.message(Command(commands = 'command04'))
async def process_command_04(message: Message):
    await message.answer(
        text = 'four?',
        reply_markup=my_keyboard_4
    )

@dp.message(Command(commands = 'command05'))
async def process_command_05(message: Message):
    await message.answer(
        text = 'fifth?',
        reply_markup=my_keyboard_5
    )


if __name__=='__main__':
    dp.run_polling(bot)
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

button_1 = KeyboardButton(text='Собак')
button_2 = KeyboardButton(text='Огурцов')

keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard = True,
    one_time_keyboard = True
    )

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text = 'Чего кошки боятся больше?',
        reply_markup=keyboard
    )

@dp.message(F.text=='Собак')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, наверное'
#        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.text=='Огурцов')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='И они в чём-то правы. На меня например вчера подозрительно смотрел помидор'
#        reply_markup=ReplyKeyboardRemove()
    )

if __name__=='__main__':
    dp.run_polling(bot)
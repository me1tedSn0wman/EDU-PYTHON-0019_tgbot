from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Hi!\nMy name is echobot \n Write me something')

@dp.message(Command(commands=['help']))
async def send_echo(message: Message):
    await message.answer('Write me something and i will answer you')

@dp.message()
async def send_echo(message: Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
        dp.run_polling(bot)
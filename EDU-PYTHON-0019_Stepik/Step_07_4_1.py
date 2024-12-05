from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

def my_start_filter(message: Message) -> bool:
    return message.text == '/start'

@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='That is command /start')

if __name__ == '__main__':
    dp.run_polling(bot)
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name is Echobot!\nWrite me something')

async def process_help_command(message: Message):
    await message.answer(
        'Write me something and in answer '
        'I send it back to you'
        )

async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text = 'This type is not supported by send_copy()'
            )

dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
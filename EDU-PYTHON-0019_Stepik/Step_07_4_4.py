from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F

@dp.message(Command(commands='start'))
async def process_command_start(message: Message):
    await message.answer('This is command /start')

@dp.message(Command(commands='start', prefix='|'))
async def process_command_start_2(message: Message):
    await message.answer('And that command /start')

@dp.message(CommandStart())
async def process_command_start_3(message: Message):
    await message.answer('This is command start')

lambda message: message.from_user.id = 159

F.from_user.id =17390

lambda message: not message.text.startwitch('Привет')

lambda message: not message.content_type in {
    ContentType.PHOTO,
    ContentType.VIDEO,
    ContentType.AUDIO,
    ContentType.DOCUMENT
    }
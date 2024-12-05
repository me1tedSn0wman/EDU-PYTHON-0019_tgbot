from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Any


BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers= []

        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',','').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))

            if numbers:
                return {'numbers': numbers}
            return False

@dp.message(F.text.lower().startswith('Find numbers'), NumbersInMessage())
async def process_if_numbers(message:Message, numbers: list[int]):
    await message.answer(text=f'Found: {", ".join(str(num) for num in numbers)}')

@dp.message(F.text.lower().startwith('Find numbers'))
async def process_if_not_numbers(message: Message):
    await message.answer(
        text='Not found anything =('
        )

class MyFilter(BaseFilter):
    async def __call__(self, message: Message)-> bool | dict[str, Any]:

        return {'key_1': 'value_1',
                'key_2': 'value_2',
                'key_3': 'value_3'
                }

@dp.message(MyFilter())
async def some_handler(
    message: Message,
    key_1: str,
    key_2: str,
    key_3: str
    ):
    await time.sleep(1)

@dp.message(F.photo[0].as_('photo_min'))
async def process_photo_send(message: Message, photo_min: PhotoSize):
    print(photo_min)
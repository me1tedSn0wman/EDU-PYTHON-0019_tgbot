from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

admin_ids: list[int] = [1789685485]

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int])-> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='You are admin')

@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='You aren\'t admin')

if __name__ == '__main__':
    dp.run_polling(bot)
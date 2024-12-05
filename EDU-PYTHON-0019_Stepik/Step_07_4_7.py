from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message


BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


#
#class NumbersInMessage(BaseFilter):
#    async def __call__(self, message: Message) -> bool | dict[str,list[int]]:
#        numbers= []
#
#        for word in message.text.split():
#            normalized_word = word.replace('.', '').replace(',','').strip()
#            if normalized_word.isdigit():
#                numbers.append(int(normalized_word))
#
#            if numbers:
#                return {'numbers': numbers}
#            return False

class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем словарь со списком чисел по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False


@dp.message(F.text.lower().startswith('найди'), NumbersInMessage())
async def process_if_numbers(message:Message, numbers: list[int]):
    print('this')
    await message.answer(text=f'Found: {", ".join(str(num) for num in numbers)}')

@dp.message(F.text.lower().startswith('найди'))
async def process_if_not_numbers(message: Message):
    print('that')
    await message.answer(
        text='Not found anything =('
        )
    
#@dp.message()
#async def answer_if_not_admins_update(message: Message):
#    print('those')
#    await message.answer(text='i\'m alive')

if __name__ == '__main__':
    dp.run_polling(bot)
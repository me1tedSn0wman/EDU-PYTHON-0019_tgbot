#
# Callback factory
#

from aiogram.filters.callback_data import CallbackData


from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder # Builder for inline buttons 

################

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

################

class MyCallbackFactory(CallbackData, prefix='anu'):
    a: str
    b: int
    c: int
    d: str

class GoodsCallbackFactory(CallbackData, prefix ='goods'):
    category_id: int
    subcategory_id: int
    item_id: int

############

button_1 = InlineKeyboardButton(
    text = 'Категория 1',
    callback_data = GoodsCallbackFactory(
        category_id = 1,
        subcategory_id = 0,
        item_id = 0
    ).pack()
)

button_2 = InlineKeyboardButton(
    text = 'Kaтегория 2',
    callback_data = GoodsCallbackFactory(
        category_id = 2,
        subcategory_id = 0,
        item_id = 0
    ).pack()
)

markup = InlineKeyboardMarkup(
    inline_keyboard = [[button_1],[button_2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text = 'Вот такая клавиатура',
        reply_markup = markup
    )

@dp.callback_query(GoodsCallbackFactory.filter(F.category_id == 1))
async def process_any_inline_button_press(
    callback: CallbackQuery,
    callback_data: GoodsCallbackFactory
    ):
    await callback.message.answer(text = 'Just cetegory 1')
    await callback.message.answer(text = callback_data.pack())
    await callback.answer()

@dp.callback_query(GoodsCallbackFactory.filter())
async def process_any_inline_button_press(
    callback: CallbackQuery,
    callback_data: GoodsCallbackFactory
    ):
    await callback.message.answer(
        text = f'Категория товаров: {callback_data.category_id}\n' \
               f'Подкатегория товаров: {callback_data.subcategory_id}\n' \
               f'Товар: {callback_data.item_id}'

    )
    await callback.answer()

@dp.callback_query()
async def process_any_inline_button_press(callback: CallbackQuery):
    print(callback.model_dump_json(indent=4, exclude_none=True))
    await callback.answer()

if __name__ == '__main__':
    dp.run_polling(bot)
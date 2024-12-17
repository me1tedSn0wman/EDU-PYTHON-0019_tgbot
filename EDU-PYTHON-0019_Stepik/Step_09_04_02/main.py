#
# Inline Buttons
#

from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder # Builder for inline buttons 

################

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

################

big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text = 'Это инлайн-кнопки. Нажми на любую!',
        reply_markup = keyboard
    )

@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_buttons_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text = 'Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup = callback.message.reply_markup
        )
    await callback.answer(
        text='!!! Нажата кнопка 1!!!'
        )

@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_buttons_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text = 'Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup = callback.message.reply_markup
        )
    await callback.answer(
        text = '!!! Нажата кнопка 2!!!',
        show_alert = True
        )


if __name__ == '__main__':
    dp.run_polling(bot)
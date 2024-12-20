from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    PhotoSize
)

################################

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

################################

storage = MemoryStorage()

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(storage=storage)

################################

user_dict: dict[int,dict[str, str | int| bool]] = {}

class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    upload_photo = State()
    fill_education = State()
    fill_wish_news = State()

@dp.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text =  'Этот бот демонстрирует работу FSM\n\n'
                'Чтобы перейти к заполнению анкеты - '
                'отправьте команду /fillform'
    )

@dp.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text =  'Отменять нечего. Вы вне машины состояний\n\n'
                'Чтобы перейти к заполнению анкеты - '
                'отправьте команду /fillform'
    )

@dp.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text =  'Вы вышли из машины состояний\n\n'
                'Чтобы снова перейти к заполнению анкеты - '
                'отправьте команду /fillform'
    )
    await state.clear()

# Name Handler
@dp.message(Command(commands='fillform'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(
        text = 'Пожалуйста, введите ваше имя'
    )
    await state.set_state(FSMFillForm.fill_name)

# Age Handler
@dp.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')

    await state.set_state(FSMFillForm.fill_age)

@dp.message(StateFilter(FSMFillForm.fill_name))
async def warning_not_name(message: Message):
    await message.answer(
        text =  'То, что вы отправили не похоже на имя\n\n'
                'Пожалуйста, введите ваше имя\n\n'
                'Если вы хотите прервать заполнение анкеты - '
                'отправьте команду /cancel'
    )

# After Age Check fillings was good
@dp.message(StateFilter(FSMFillForm.fill_age),
            lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(age=message.text)

    male_button = InlineKeyboardButton(
        text = 'Мужской ♂',
        callback_data = 'male'
    )
    female_button = InlineKeyboardButton(
        text = 'Женский ♀',
        callback_data = 'female' 
    )
    undefined_button = InlineKeyboardButton(
        text = '🤷 Пока не ясно',
        callback_data = 'undefined_gender' 
    )

    keyboard: list[list[InlineKeyboardButton]] = [
        [male_button, female_button],
        [undefined_button]
    ]

    markup = InlineKeyboardMarkup(inline_keyboard = keyboard)

    await message.answer(
        text =  'Спасибо!\n\nУкажите ваш пол',
        reply_markup = markup
    )
    await state.set_state(FSMFillForm.fill_gender)

#when age filling goes wrong
@dp.message(StateFilter(FSMFillForm.fill_age))
async def warning_not_age(message: Message):
    await message.answer(
        text =  'Возвраст должен быть целым числом от 4 до 120\n\n'        
                'Попробуйте ещё раз\n\n Если вы хотите прервать '
                'заполнение анкеты - отправьте команду /cancel'
    )

@dp.callback_query(StateFilter(FSMFillForm.fill_gender),
                   F.data.in_(['male', 'female', 'undefined_gender']))
async def process_gender_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender = callback.data)
    await callback.message.delete()
    await callback.message.answer(
        text =  'Спасибо! А теперь загрузите, пожалуйста, ваше фото'
    )
    await state.set_state(FSMFillForm.upload_photo)

@dp.message(StateFilter(FSMFillForm.fill_gender))
async def warning_not_gender(message: Message):
    await message.answer(
        text =  'Пожалуйста, пользуйтесь кнопками '
                'при выборе пола\n\nЕсли вы хотите прервать '
                'заполнение анкеты - отправьте команду /cancel'
    )

#After check photo
@dp.message(StateFilter(FSMFillForm.upload_photo), F.photo[-1].as_('largest_photo'))
async def process_photo_sent(
    message: Message,
    state: FSMContext,
    largest_photo: PhotoSize
    ):
    await state.update_data(
        photo_unique_id = largest_photo.file_unique_id,
        photo_id=largest_photo.file_id
    )

    secondary_button = InlineKeyboardButton(
        text = 'Среднее',
        callback_data = 'secondary'
    )
    higher_button = InlineKeyboardButton(
        text = 'Высшее',
        callback_data = 'higher'
    )
    no_edu_button = InlineKeyboardButton(
        text = '🤷 Нету',
        callback_data = 'no_edu'
    )

    keyboard: list[list[InlineKeyboardButton]] = [
        [secondary_button, higher_button],
        [no_edu_button]
    ]

    markup = InlineKeyboardMarkup(inline_keyboard = keyboard)

    await message.answer(
        text = 'Спасибо!\n\nУкажите ваше образование',
        reply_markup=markup
    )

    await state.set_state(FSMFillForm.fill_education)

#something goes wrong on photo checkpoint
@dp.message(StateFilter(FSMFillForm.upload_photo))
async def warning_not_photo(message: Message):
    await message.answer(
        text =  'Пожалуйста, на этом шаге отправьте '
                'ваше фото\n\nЕсли вы хотите прервать '
                'заполнение анкеты - отправьте команду /cancel'
    )

@dp.callback_query(StateFilter(FSMFillForm.fill_education),
                   F.data.in_(['secondary', 'higher', 'no_edu']))
async def process_education_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(education=callback.data)

    yes_news_button = InlineKeyboardButton(
        text = 'Да',
        callback_data = 'yes_news'
    )
    no_news_button = InlineKeyboardButton(
        text = 'Нет, спасибо',
        callback_data = 'no_news'
    )

    keyboard: list[list[InlineKeyboardButton]] = [
        [yes_news_button, no_news_button]
    ]

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await callback.message.edit_text(
        text =  'Спасибо!\n\nОстался последний шаг.\n'
                'Хотели бы вы получать новости?',
        reply_markup = markup
    )

    await state.set_state(FSMFillForm.fill_wish_news)

@dp.message(StateFilter(FSMFillForm.fill_education))
async def warning_not_education(message: Message):
    await message.answer(
        text =  'Пожалуйста, пользуйтесь кнопками при выборе образования\n\n'
                'Если вы хотите прервать заполнение анкеты - отправьте '
                'команду /cancel'
    )

@dp.callback_query(StateFilter(FSMFillForm.fill_wish_news),
            F.data.in_(['yes_news', 'no_news']))
async def process_wish_news_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(wish_news=callback.data =='yes_news')

    user_dict[callback.from_user.id] = await state.get_data()

    await state.clear()

    await callback.message.edit_text(
        text =  'Спасибо! Ваши данные сохранены!\n\n'
                'Вы вышли из машины состояний'
    )

    await callback.message.answer(
        text =  'Чтобы посмотреть данные вашей '
                'анкеты - отправьте команду /showdata'
    )

@dp.message(StateFilter(FSMFillForm.fill_wish_news))
async def warning_not_wish_news(message: Message):
    await message.answer(
        text =  'Пожалуйста, воспользуйтесь кнопками!\n\n'
                'Если вы хотите прервать заполнение анкеты - '
                'отправьте команду /cancel'
    )

@dp.message(Command(commands='showdata'), StateFilter(default_state))
async def process_showdata_command(message: Message):
    if message.from_user.id in user_dict:
        await message.answer_photo(
            photo = user_dict[message.from_user.id]['photo_id'],
            caption =   f'Имя: {user_dict[message.from_user.id]["name"]}\n'
                        f'Возраст: {user_dict[message.from_user.id]["age"]}\n'
                        f'Пол: {user_dict[message.from_user.id]["gender"]}\n'
                        f'Образование: {user_dict[message.from_user.id]["education"]}\n'
                        f'Получать новости: {user_dict[message.from_user.id]["wish_news"]}'

        )
    else:
        await message.answer(
            text =  'Вы еще не заполняли анкету. Чтобы приступить - '
                    'отправьте команду /fillform'   
        )

@dp.message(StateFilter(default_state))
async def send_echo(message: Message):
    await message.reply(text='Извините, пошло что-то не так')

if __name__ == '__main__':
    dp.run_polling(bot)
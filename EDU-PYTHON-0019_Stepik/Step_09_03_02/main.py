from aiogram import Bot, Dispatcher
from set_menu import set_main_menu

async def main():

    bot = Bot(
        token = config.tg_bot.token,
        parse_mode = 'HTML'
        )
    dp = Dispatcher()

    await set_main_menu(bot)
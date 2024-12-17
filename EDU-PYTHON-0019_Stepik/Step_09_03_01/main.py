#
# Menu Buttons
#

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command = '/help',
                   description = 'Справка по работе бота'
                   ),
        BotCommand(command = '/support',
                   description = 'Поддержка'
                   ),
        BotCommand(command = '/contacts',
                   description = 'Другие способы связи'
                   ),
        BotCommand(command = '/payments',
                   description = 'Платежи'
                   )
    ]

    await bot.set_my_commands(main_menu_commands)

dp.startup.register(set_main_menu)

dp.run_polling(bot)
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5

users = {}

def get_random_number() -> int:
    return random.randint(1,100)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Hello, \n let\'s play game "guess number"?\n\n'
        'To get game rules and get a list of available commands, send command /help'
        )
    if message.from_user.id not in users:
        users[message.from_user.id]= {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
            }

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        f'Game rule: I guess number from 1 to 100, '
        f'and you should guess it\n You gave {ATTEMPTS} '
        f'attempts\n\nAvailable Commands:\n /help - rules and list of commands'
        f'/cancel - exit from game\n'
        f'/stat - look up for the stat\n'
        f'let\'s play a game'
        )

@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    await message.answer(
        f'All games played: {users[message.from_user.id]["total_games"]}\n'
        f'Games win: {users[message.from_user.id]["wins"]}'
        )

@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
       users[message.from_user.id]['in game'] = False
       await message.answer(
           'you exit from the game, if you want play again'
           ' - write it'
           )
    else:
        await message.answer(
            'We don\'t play anyway\n'
            'Maybe wanna play?'
            )

  
@dp.message(F.text.lower().in_(['yes', 'ok', 'let\'s go', 'play', 'let\'s play']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game']=True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] =ATTEMPTS
        await message.answer(
            'well, i guess number from 1 to 100, '
            'try to guess!'
            )
    else:
        await message.answer(
            'While we play this game, i can react only to number from 1 to 100'
            ' and commands /cancel and /stat'
            )

@dp.message(F.text.lower().in_(['nay', 'no', 'don\'t']))
async def process_number_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer(
            'well, ok, nevermind'
            )
    else:
        await message.answer(
            'We are playing right now'
            )


@dp.message(lambda x: x.text and x.text.isdigit() and 1<=int(x.text) <=100)
async def process_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['in_game']= False
            users[message.from_user.id]['total_games']+=1
            users[message.from_user.id]['wins']+=1
            await message.answer(
                'Yay! you guessed the answer!\n\n'
                'Maybe play another time?'
                )
        elif int(message.text) > user['secret_number']:
            users[message.from_user.id]['attempts'] -=1
            await message.answer('My number is less')
        elif int(message.text) < user['secret_number']:
            users[message.from_user.id]['attempts'] -=1
            await message.answer('My number is more')

        if users[message.from_user.id]['attempts']==0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(
                f'Sorry, but you run out of attemps'
                f'My number was {users[message.from_user.id]["secret_number"]}'
                f'let\'s play another round'
                )
    else:
        await message.answer('We dont play. Do you want to play?')

@dp.message()
async def process_other_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer(
            'We are playing right now'
            'Please, send numbers from 1 to 100'
            )
    else:
        await message.answer(
            'i can just play games\n'
            'let play game'
            )

if __name__ == "__main__":
    dp.run_polling(bot)

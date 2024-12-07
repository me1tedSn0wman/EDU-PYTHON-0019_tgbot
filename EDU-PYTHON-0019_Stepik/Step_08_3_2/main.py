import os

from environs import Env

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')
admin_id = env.int('ADMIN_ID')

print(bot_token)
print(admin_id)
print()

print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))
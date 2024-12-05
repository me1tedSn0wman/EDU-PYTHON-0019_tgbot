import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7715698078:AAGuFLB_eyR71fCw_93gzdLAXX4K1kpdWfs'

offset = -2
timeout = -5
updates: dict

def do_smth() -> None:
    print('Was Update')

while True:
    start_time = time.time()

    print('while...')
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_smth()

    time.sleep(1)
    end_time = time.time()
    print(f'Time between requests to Telegram API:{end_time-start_time}')
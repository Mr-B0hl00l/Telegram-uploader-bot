import os
import asyncio
import telegram
import argparse
from datetime import datetime
import pytz


YELLOW = '\033[93m'
PURPLE = '\033[0;35m'
ENDC = '\033[0m'
RED = '\033[91;1m'
GREEN = '\033[92m'

banner = f'''{YELLOW}
88888888888       888
    888           888
    888           888
    888   .d88b.  888  .d88b.   .d88b.  888d888 8888b.  88888b.d88b.
    888  d8P  Y8b 888 d8P  Y8b d88P"88b 888P"      "88b 888 "888 "88b
    888  88888888 888 88888888 888  888 888    .d888888 888  888  888
    888  Y8b.     888 Y8b.     Y88b 888 888    888  888 888  888  888
    888   "Y8888  888  "Y8888   "Y88888 888    "Y888888 888  888  888
                                    888
                               Y8b d88P
                                "Y88P"
                  888                        888                       888               888
                  888                        888                       888               888
                  888                        888                       888               888
888  888 88888b.  888  .d88b.   8888b.   .d88888  .d88b.  888d888      88888b.   .d88b.  888888
888  888 888 "88b 888 d88""88b     "88b d88" 888 d8P  Y8b 888P"        888 "88b d88""88b 888
888  888 888  888 888 888  888 .d888888 888  888 88888888 888          888  888 888  888 888
Y88b 888 888 d88P 888 Y88..88P 888  888 Y88b 888 Y8b.     888          888 d88P Y88..88P Y88b.
 "Y88888 88888P"  888  "Y88P"  "Y888888  "Y88888  "Y8888  888          88888P"   "Y88P"   "Y888
         888
         888
         888
{ENDC}
{PURPLE}                Created by Mr-B0hl00l {ENDC}
'''
print(banner)
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', metavar="File.txt",help='File path to send')
parser.add_argument('-d', '--directory', metavar="Directory1/directory2/",help='Directory path to send')
args = parser.parse_args()


chat_id = '' #Insert chat_id here
bot_token = '' #Insert bot_token here
bot = telegram.Bot(token=bot_token)

async def send_file(file):
    await bot.send_document(chat_id, document=open(file, 'rb'))

async def send_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            await bot.send_document(chat_id, document=open(file_path, 'rb'))
            await asyncio.sleep(1)

async def main():
    
    if not bot_token or not chat_id:
        print(f'{RED}Please enter telegram bot token or chat id in Telegram-uploader-bot.py{ENDC}\t\n')
        exit()
    success = False
    if args.file:
        await send_file(args.file)
        success = True
    if args.directory:
        await send_directory(args.directory)
        success = True
    if success:
        print(f'{GREEN}File or directory uploaded successfully{ENDC}\t\n')
    else:
        print(f'{RED}File or directory not uploaded{ENDC}\t\n')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
loop.close()

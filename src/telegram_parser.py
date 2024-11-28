import os
import pprint
from telethon import TelegramClient
from yadisk.exceptions import PathExistsError

from src import config
from src.logger import add_photo_to_log, get_all_ids
from src.yadisk_repo import upload_to_yadisk

DOWNLOAD_PATH = 'photos'
CHANNEL_FILES_LIMIT = 15
os.makedirs(DOWNLOAD_PATH, exist_ok=True)


async def parse_telegram_channels() -> int:
    count = 0
    checked = await get_all_ids()
    async with TelegramClient('session_name', config.API_ID, config.API_HASH,
                              system_version='4.16.30-vxCUSTOM') as client:
        for channel in config.CHANNELS:
            messages = await client.get_messages(channel, limit=CHANNEL_FILES_LIMIT)
            for message in messages:
                if message.photo:
                    filename = message.photo.id
                    if filename in checked:
                        continue
                    file_path = await client.download_media(message.photo, DOWNLOAD_PATH)
                    try:
                        await upload_to_yadisk(filename, file_path)
                        print(f"file {filename} add to temp")
                        await add_photo_to_log(filename)
                        count += 1
                    except PathExistsError:
                        print(f"file {filename} already exist")
                    os.remove(file_path)
    return count
import os

from telethon import TelegramClient

from src import config
from src.yadisk_repo import upload_to_yadisk

DOWNLOAD_PATH = 'photos'

os.makedirs(DOWNLOAD_PATH, exist_ok=True)


async def parse_telegram_channels():
    async with TelegramClient('session_name', config.API_ID, config.API_HASH,
                              system_version='4.16.30-vxCUSTOM') as client:
        for channel in config.CHANNELS:
            messages = await client.get_messages(channel, limit=2)
            for message in messages:
                # secs = datetime.now().timestamp() - message.date.timestamp()
                # hours = round(secs / 60 / 60)
                if message.photo:
                    filename = f"{channel.split("/")[-1]}_{message.date.strftime("%d-%b-%Y_%H:%M:%S")}"
                    file_path = await client.download_media(message.photo, DOWNLOAD_PATH)
                    await upload_to_yadisk(filename, file_path)
                    os.remove(file_path)

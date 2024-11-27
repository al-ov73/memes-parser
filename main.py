
import os
import asyncio
import yadisk
from datetime import datetime, timedelta
from dotenv import load_dotenv

from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHANNEL = os.getenv("CHANNEL")
YA_TOKEN = os.getenv("YA_TOKEN")
CHANNELS = os.getenv("CHANNELS").split(' ')

DOWNLOAD_PATH = 'photos'

os.makedirs(DOWNLOAD_PATH, exist_ok=True)

async def upload_to_yadisk(filepath):
    client = yadisk.Client(token=YA_TOKEN)
    with client:
        with open(filepath, "rb") as f:
            client.upload(f, f"memes/temp/{filepath}")
        
async def main():
    async with TelegramClient('session_name', API_ID, API_HASH, system_version='4.16.30-vxCUSTOM') as client:
        for channel in CHANNELS:
            messages = await client.get_messages(channel, limit=2)
            for message in messages:
                # secs = datetime.now().timestamp() - message.date.timestamp()
                # hours = round(secs / 60 / 60)
                if message.photo:
                    file_path = await client.download_media(message.photo, DOWNLOAD_PATH)
                    print(file_path)
                    await upload_to_yadisk(file_path)           
        
if __name__ == "__main__":
    asyncio.run(main())
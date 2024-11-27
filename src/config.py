import os

from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHANNEL = os.getenv("CHANNEL")
YA_TOKEN = os.getenv("YA_TOKEN")
CHANNELS = os.getenv("CHANNELS").split(' ')

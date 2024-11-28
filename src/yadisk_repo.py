import yadisk
import pprint
from yadisk.objects import SyncResourceObject

from src import config

TEMP_PATH = "memes/temp/"
STORAGE_PATH = "memes/storage/"

async def upload_to_yadisk(filename: str, filepath: str) -> None:
    client = yadisk.Client(token=config.YA_TOKEN)
    with client:
        with open(filepath, "rb") as f:
            client.upload(f, f"{TEMP_PATH}{filename}.jpg")


async def get_temp_links() -> list[dict]:
    client = yadisk.Client(token=config.YA_TOKEN)
    with client:
        files_list = list(client.listdir(TEMP_PATH))
        files = []
        for file in files_list:
            new_file = {
                "filename": file.name,
                "preview": file.preview,
                "url": file.file,
            }
            files.append(new_file)
        return files

async def get_links() -> list[dict]:
    client = yadisk.Client(token=config.YA_TOKEN)
    with client:
        files_list = list(client.listdir(STORAGE_PATH))
        files = []
        for file in files_list:
            new_file = {
                "filename": file.name,
                "preview": file.preview,
                "url": file.file,
            }
            files.append(new_file)
        return files
    
async def move_to_storage(filename: str) -> None:
    client = yadisk.Client(token=config.YA_TOKEN)
    with client:
        from_path = f"{TEMP_PATH}{filename}"
        to_path = f"{STORAGE_PATH}{filename}"
        client.move(from_path, to_path)
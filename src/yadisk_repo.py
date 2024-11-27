import yadisk
from yadisk.objects import SyncResourceObject

from src import config


async def upload_to_yadisk(filename: str, filepath: str) -> None:
    client = yadisk.Client(token=config.YA_TOKEN)
    with client:
        with open(filepath, "rb") as f:
            client.upload(f, f"memes/temp/{filename}")


async def get_links() -> list[SyncResourceObject]:
    client = yadisk.Client(token=config.YA_TOKEN)
    with client:
        files_list = list(client.listdir("memes/temp"))
        return [file.file for file in files_list if file.file]

async def add_photo_to_log(filename):
    with open("log.txt", "a") as file:
        file.write(f"{filename}\n")


async def get_all_ids():
    with open("log.txt", "r") as file:
        lines = file.readlines()
    return lines

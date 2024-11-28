from importlib.metadata import files

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.telegram_parser import parse_telegram_channels
from src.yadisk_repo import get_temp_links, get_links, move_to_storage

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/temp", response_class=HTMLResponse)
async def index_view(request: Request):
    images = await get_temp_links()
    context = {
        "images": images,
    }
    return templates.TemplateResponse(request=request, name="temp.html", context=context)

@app.get("/", response_class=HTMLResponse)
async def index_view(request: Request):
    images = await get_links()
    context = {
        "images": images,
    }
    return templates.TemplateResponse(request=request, name="index.html", context=context)

@app.post("/", response_class=RedirectResponse)
async def index_view(request: Request):
    files_added = await parse_telegram_channels()
    print(f"added {files_added} files")
    return RedirectResponse("/", status_code=302)

@app.post("/store/{filename}", response_class=RedirectResponse)
async def index_view(request: Request, filename: str):
    await move_to_storage(filename)
    print(f"file {filename} moved to storage")
    return RedirectResponse("/", status_code=302)
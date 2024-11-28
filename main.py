from importlib.metadata import files

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.telegram_parser import parse_telegram_channels
from src import yadisk_repo

app = FastAPI()

templates = Jinja2Templates(directory="templates")
store_repo = yadisk_repo

@app.get("/temp", response_class=HTMLResponse)
async def index_view(request: Request):
    images = await store_repo.get_temp_links()
    context = {
        "images": images,
    }
    return templates.TemplateResponse(request=request, name="temp.html", context=context)

@app.get("/", response_class=HTMLResponse)
async def index_view(request: Request):
    images = await store_repo.get_links()
    context = {
        "images": images,
    }
    return templates.TemplateResponse(request=request, name="index.html", context=context)

@app.post("/", response_class=RedirectResponse)
async def index_view(request: Request):
    await store_repo.parse_telegram_channels()
    return RedirectResponse("/", status_code=302)

@app.post("/store/{filename}", response_class=RedirectResponse)
async def index_view(request: Request, filename: str):
    print(filename)
    await store_repo.move_to_storage(filename)
    return RedirectResponse("/", status_code=302)
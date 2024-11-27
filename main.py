from importlib.metadata import files

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.telegram_parser import parse_telegram_channels
from src.yadisk_repo import get_links

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index_view(request: Request):
    links = await get_links()
    context = {
        "links": links,
    }
    return templates.TemplateResponse(request=request, name="index.html", context=context)


@app.post("/", response_class=RedirectResponse)
async def index_view(request: Request):
    await parse_telegram_channels()
    return RedirectResponse("/", status_code=302)

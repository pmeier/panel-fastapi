import panel as pn
from bokeh.embed import server_document
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app import template

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


@app.get("/")
async def bkapp_page(request: Request):
    script = server_document("http://127.0.0.1:5000/")
    return templates.TemplateResponse(
        "base.html", {"request": request, "script": script}
    )


pn.serve(
    {"/": template},
    port=5000,
    allow_websocket_origin=["127.0.0.1:8000"],
    address="127.0.0.1",
    show=False,
)

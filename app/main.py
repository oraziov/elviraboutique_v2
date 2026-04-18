from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services import get_products_full

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    products = get_products_full(10)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "products": products}
    )

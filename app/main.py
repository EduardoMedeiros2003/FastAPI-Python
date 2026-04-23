from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.rotas import cliente
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory='templates')


app = FastAPI(
    title='Techlog Solution API',
    description='CRM para techlog Solution',
    version='1.0.0',
)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(cliente.router)

@app.get("/health")
def read_root():
    return {"mensagem": "Olá, senhor. Sua API está funcionando."}

@app.get("/", response_class=HTMLResponse)
async def front_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "titulo": "Techlog Solutions CRM", "versao": "1.0.0"})
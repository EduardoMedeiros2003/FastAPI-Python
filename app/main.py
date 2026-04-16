from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.rotas import cliente

app = FastAPI(
    title='Techlog Solution API',
    description='CRM para techlog Solution',
    version='1.0.0',
)

app.include_router(cliente.router)

@app.get("/")
def read_root():
    return {"mensagem": "Olá, senhor. Sua API está funcionando."}

@app.get('/front', response_class=HTMLResponse)
async def front_page():
    return """
    <html>
        <head>
            <title>Techlog Solutions</title>
        </head>
        <body>
            <h1>🔪 Techlog Solutions</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
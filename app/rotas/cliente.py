from fastapi import APIRouter
from app.modelos.cliente import Cliente

router = APIRouter(
    prefix="/clientes"
)

@router.get('/', response_model=list[Cliente])
async def listar_clientes():
    clientes_list = [Cliente(nome='Raphael', email='rafael@rossi.com', telefone='1234567'), Cliente(nome='Eduardo', email='eduardo@rossi.com', telefone='12132435')]
    

    return clientes_list
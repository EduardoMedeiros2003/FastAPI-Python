from fastapi import APIRouter
from app.modelos.cliente import Cliente

CLIENTE_LIST = [Cliente(id_=1,nome='Raphael', email='rafael@rossi.com', telefone='1234567'), Cliente(id_=2, nome='Eduardo', email='eduardo@rossi.com', telefone='12132435')]

router = APIRouter(
    prefix="/clientes"
)

@router.get('/', response_model=list[Cliente])
async def listar_clientes():
    
    return CLIENTE_LIST

@router.get('/{cliente_id}', response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENTE_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    return None
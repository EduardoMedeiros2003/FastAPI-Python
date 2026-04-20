from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from app.modelos.cliente import Cliente, ClienteCriarAtualizar
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio

CLIENTE_LIST = [Cliente(id_=1,nome='Raphael', email='rafael@rossi.com', telefone='1234567'), Cliente(id_=2, nome='Eduardo', email='eduardo@rossi.com', telefone='12132435')]

router = APIRouter(
    prefix="/clientes"
)

@router.get('/', response_model=list[Cliente])
async def listar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()
    

@router.get('/{cliente_id}', response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENTE_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    return None

async def obter_cliente(self, cliente_id: int) -> Cliente | None:
    with self.bd.conectar() as conexao:# Faz conecxão com o banco de dados
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, email, telefone FROM clientes WHERE id = ?", (cliente_id,)
        )
        linha = cursor.fetchone()
        if linha:
            return Cliente(id=linha[0], nome=linha[1], email=linha[2], telefone=linha[3])
        
        async def obter_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int
):
            cliente = await cliente_repositorio.obter_cliente(cliente_id)

            if not cliente:
                raise HTTPException(status_code=404, detail="Cliente não encontrado!")
        
            return cliente
        
@router.post("/", response_model=Cliente, status_code=201)
async def criar_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente: ClienteCriarAtualizar
):
    return await cliente_repositorio.criar_cliente(cliente)

@router.put("/{cliente_id}", response_model=Cliente | None)
async def atualizar_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int,
    cliente: ClienteCriarAtualizar
):
    cliente_atualizado = await cliente_repositorio.atualizar_cliente(cliente_id, cliente)
    if not cliente_atualizado:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return cliente_atualizado

@router.delete("/{cliente_id}", status_code=204)
async def deletar_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int
):
    sucesso = await cliente_repositorio.deletar_cliente(cliente_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")

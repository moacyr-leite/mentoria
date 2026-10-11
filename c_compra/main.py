from fastapi import FastAPI
from pydantic import BaseModel
from data_manage import read_data, white_data

class Produto(BaseModel):
    id: int
    nome: str
    preco: int
    quantidade: int

app = FastAPI()

@app.get("/estoque/")
async def get_estoque():
    return read_data("estoque")

@app.post("/estoque/")
async def add_produto(produto:Produto):
    return

@app.delete("/estoque/")
async def delete_produto():
    return

@app.get("/carrinho/")
async def get_carrinho():
    return

@app.post("/carrinho/")
async def add_ao_carrinho(produto:Produto):
    return


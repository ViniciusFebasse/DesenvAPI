"""
TODO: DESENVOLVIMENTO DE API'S
-> pip install fastapi
-> pip install uvicorn
"""

# Importação das dependências
from fastapi import FastAPI
from pydantic import BaseModel

from db import BancoDeDados

# Criação de uma instância de FastAPI
app = FastAPI()

banco = BancoDeDados()
registros = banco.registros()
especifico = banco.especifico("Mathias")

# Definição da rota raíz
@app.get("/")
def raiz():
    return especifico
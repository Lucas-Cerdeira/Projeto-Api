
from fastapi import FastAPI

from pydantic import BaseModel




class Usuario(BaseModel):
    nome: str
    idade: int


app = FastAPI()


BANCO_DE_DADOS = []


@app.post("/Pessoa")
def add_pessoa(usuario: Usuario):
    BANCO_DE_DADOS.append(usuario)
    with open('Lista_Pessoas.txt', 'a') as arquivo:
        arquivo.write(str(usuario) + '\n')
        return str(usuario)



@app.get("/Pessoas")
def ver_pessoas():
    with open('Lista_Pessoas.txt', 'r') as arquivo:
        BANCO_DE_DADOS.clear()
        for pessoas in arquivo:
            BANCO_DE_DADOS.append(pessoas[0:-1])

        return BANCO_DE_DADOS




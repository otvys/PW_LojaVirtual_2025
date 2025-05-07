from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data import cliente_repo, produto_repo


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
produto_repo.criar_tabela()
cliente_repo.criar_tabela()


@app.get("/")
async def root():
    produtos = produto_repo.obter_todos()
    response = templates.TemplateResponse("index.html", {"request": {}, "produtos": produtos})
    return response

@app.get("/clientes")
async def root():
    clientes = cliente_repo.obter_todos()
    response = templates.TemplateResponse("clientes.html", {"request": {}, "clientes": clientes})
    return response


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)    
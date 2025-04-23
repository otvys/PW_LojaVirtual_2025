# Programação para a Web

#### Aula 07: Introdução ao Desenvolvimento Web com FastAPI e Jinja2 

#### Prof. Ricardo Maroquio

### Objetivos da Aula 
 
- **Introduzir o FastAPI** : Entender sua proposta, estrutura e como criar rotas que retornam conteúdo HTML.
 
- **Utilizar Jinja2 com FastAPI** : Aprender a renderizar templates Jinja2 para gerar páginas dinâmicas.
 
- **Integrar com SQLite** : Demonstrar como acessar dados armazenados em um banco SQLite e exibi-los nas páginas, utilizando conceitos já conhecidos (sem ORM, com Pydantic quando necessário).

### Pré-requisitos 
 
- Conhecimento básico de Python.
 
- Experiência com manipulação de SQLite (sem ORM) e uso de classes Pydantic.
 
- Ambiente de desenvolvimento configurado (preferencialmente com VSCode, PyCharm ou similar).

#### 1. Introdução
 
- **Contextualização** :
 
  - Apresentar o FastAPI, destacando sua performance, simplicidade e capacidade de trabalhar com APIs e também com páginas HTML.
 
  - Discutir a escolha de utilizar Jinja2 para renderização de templates.
 
- **Exemplos de Aplicação** :
 
  - Mostrar rapidamente casos de uso: sites dinâmicos, dashboards, listagens de dados.


#### 2. Configuração do Ambiente

 
- **Instalação de Dependências** :
 
  - Comando para instalar FastAPI, Uvicorn e Jinja2:

```bash
pip install fastapi uvicorn jinja2
```
 
- **Estrutura do Projeto** :
 
  - Organize os diretórios:

```css
projeto_fastapi/
  ├── main.py
  └── templates/
      ├── index.html
      └── items.html
```
 
- **Explicação Rápida** :
 
  - Por que separar os templates e como o FastAPI irá buscá-los.


#### 3. Criando uma Aplicação FastAPI Básica (15 minutos) 

 
- **Código Inicial** :
 
  - Apresentar um exemplo mínimo:



```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})
```
 
- **Demonstração** :
 
  - Executar o servidor com:



```bash
uvicorn main:app --reload
```
 
  - Visualizar a página inicial.


#### 4. Introduzindo o Jinja2 (20 minutos) 

 
- **Conceitos Básicos do Jinja2** :
 
  - Variáveis, laços, condicionais e herança de templates.
 
- **Exemplo de Template**  (`templates/index.html`):


```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Bem-vindo ao FastAPI com Jinja2</h1>
    <p>Esta é a página inicial.</p>
    <a href="/items">Ver itens</a>
</body>
</html>
```
 
- **Integração Dinâmica** :
 
  - Mostrar como passar dados do backend para o template (ex.: título, mensagens).


#### 5. Introduzindo Integração com Banco de Dados SQLite (30 minutos) 

 
- **Visão Geral do SQLite** :
 
  - Lembrar os alunos de como conectar, executar queries e fechar conexões.
 
- **Função para Conexão com SQLite** :


```python
import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # Para acessar colunas por nome
    return conn
```
 
- **Criando uma Tabela e Inserindo Dados** :
 
  - Mostre um script SQL básico (ou explique via Python) para criar uma tabela `items` e inserir alguns registros.
 
- **Exemplo de Rota com Dados do Banco** :


```python
@app.get("/items", response_class=HTMLResponse)
async def read_items(request: Request):
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})
```
 
- **Exemplo de Template para Exibir Dados**  (`templates/items.html`):


```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Lista de Itens</title>
</head>
<body>
    <h1>Itens</h1>
    <ul>
        {% for item in items %}
            <li>{{ item['id'] }} - {{ item['nome'] }}</li>
        {% else %}
            <li>Nenhum item encontrado.</li>
        {% endfor %}
    </ul>
    <a href="/">Voltar</a>
</body>
</html>
```


#### 6. Demonstração e Atividade Prática (20 minutos) 

 
- **Exercício Prático** :
 
  - Dividir os alunos em grupos para que implementem uma rota adicional (por exemplo, detalhes do item com base em um ID passado na URL).
 
  - Orientar a criar um template para exibir detalhes individuais.
 
- **Exemplo de Rota para Detalhes** :


```python
@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(item_id: int, request: Request):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    conn.close()
    return templates.TemplateResponse("item_detail.html", {"request": request, "item": item})
```
 
- **Template para Detalhes**  (`templates/item_detail.html`):


```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Detalhe do Item</title>
</head>
<body>
    {% if item %}
        <h1>{{ item['nome'] }}</h1>
        <p>ID: {{ item['id'] }}</p>
        <!-- Adicione outros campos conforme necessário -->
    {% else %}
        <h1>Item não encontrado</h1>
    {% endif %}
    <a href="/items">Voltar à lista</a>
</body>
</html>
```
 
- **Discussão** :
 
  - Incentivar os alunos a modificarem e testarem os exemplos.


#### 7. Conclusão e Dicas para Próximos Passos (10 minutos) 

 
- **Resumo do Conteúdo** :
 
  - Revisar os pontos principais: FastAPI básico, renderização de templates com Jinja2 e integração com SQLite.
 
- **Possíveis Extensões** :
 
  - Uso de formulários HTML para inserção/atualização de dados.
 
  - Introdução ao uso de Pydantic para validação de dados oriundos do usuário.
 
  - Pensar em como separar melhor as camadas da aplicação (ex.: repositório de dados).
 
- **Perguntas e Respostas** :
 
  - Abrir espaço para dúvidas e discussões.



---



### Considerações Finais 

 
- **Interatividade** : Durante a aula, incentive os alunos a explorar os códigos, modificar templates e testar diferentes queries.
 
- **Documentação e Recursos** : Recomende a leitura dos [documentos oficiais do FastAPI]()  e [do Jinja2]()  para aprofundamento.
 
- **Exercícios Complementares** : Proponha que, após a aula, os alunos adicionem novas funcionalidades ou otimizem o acesso ao banco de dados, utilizando os conceitos apresentados.


Esta abordagem deve preencher as 2 horas de aula, proporcionando uma introdução sólida e prática ao desenvolvimento web com FastAPI, Jinja2 e integração com SQLite.

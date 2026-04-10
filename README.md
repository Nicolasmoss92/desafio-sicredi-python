# Desafio Sicredi

Desafio técnico para a Cooperativa Sicredi, composto por duas questões:

**Questão 1 — Maiores devedores:** dado uma lista de contratos em aberto e uma lista de contratos já renegociados, retorna os N clientes com maior dívida que ainda não renegociaram.

**Questão 2 — Quantidade mínima de viagens:** dado uma lista de pedidos e um valor máximo por viagem, calcula o número mínimo de viagens necessárias para atender todos os pedidos, combinando o maior com o menor pedido sempre que possível.

## Requisitos

- Python 3.12+
- Dependências listadas em `requirements.txt` (FastAPI, Uvicorn, Pytest, entre outras)

## Como rodar

> Os comandos abaixo devem ser executados no **PowerShell** a partir da raiz do projeto.

**1. Criar a virtual environment**

```powershell
python -m venv venv
```

**2. Ativar a virtual environment**

```powershell
venv\Scripts\Activate.ps1
```

**3. Instalar dependências**

```bash
pip install -r requirements.txt
```

**4. Subir o servidor**

```bash
venv/Scripts/uvicorn app.main:app --reload
```

Acesse a documentação interativa em: http://127.0.0.1:8000/docs

## Como rodar com Docker

**1. Subir o container**

```bash
docker compose up --build
```

Acesse a documentação interativa em: http://127.0.0.1:8000/docs

---

## Como rodar os testes

```powershell
venv/Scripts/pytest
```

Para gerar o relatório de cobertura em HTML:

```powershell
venv/Scripts/pytest --cov=app --cov-report=html
```

O relatório será gerado na pasta `htmlcov/`. Abra o arquivo `htmlcov/index.html` no browser para visualizar.


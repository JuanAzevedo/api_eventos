# API de Eventos

Esta API gerencia eventos, permitindo operações de criação, consulta, atualização e remoção de eventos.

## Configuração

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/JuanAzevedo/api_eventos.git
cd api_eventos
pip install -r requirements.txt
```

### Execução
Execute a API localmente com:

```bash
python app.py
```
A API estará disponível em http://localhost:5000.

### Endpoints
POST /eventos: Cria um novo evento.
GET /eventos: Lista todos os eventos.
PUT /evento/<id>: Atualiza um evento existente.
DELETE /evento/<id>: Remove um evento.



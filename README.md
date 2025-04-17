# ✅ Simple Tasks

Um gerenciador de tarefas simples feito em Python, com persistência de dados usando PostgreSQL.

## 📁 Estrutura do Projeto

simple_tasks/ ├── main.py ├── src/ │ └── tasks.py # Classe TaskManager com toda a lógica de banco ├── utils/ │ └── terminal.py # Classe/função para limpar o terminal ├── .env # Variáveis de ambiente (NÃO COMITAR) ├── .gitignore ├── requirements.txt └── README.md


## 🚀 Funcionalidades

- ✅ Adicionar tarefas
- 📋 Listar tarefas
- 🔄 Alterar status (`Active`, `Inactive`, `Completed`)
- 🗑️ Deletar tarefas

## ⚙️ Requisitos

- Python 3.10+
- PostgreSQL instalado e rodando localmente
- Biblioteca `psycopg2`
- Biblioteca `python-dotenv`

Instale os requisitos com:

```bash
pip install -r requirements.txt

🔐 Variáveis de ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

DB_NAME=simple_tasks
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

⚠️ Nunca comite o arquivo .env. Ele já está listado no .gitignore.
🛠️ Como usar

No terminal:

python main.py

(No momento o main.py está vazio, mas será usado futuramente como entrada principal da aplicação)
🗃️ Banco de dados

Certifique-se de criar a tabela simple_tasks no seu banco PostgreSQL com:

CREATE TABLE simple_tasks (
    id SERIAL PRIMARY KEY,
    to_do TEXT NOT NULL,
    status TEXT NOT NULL,
    entry_time TEXT
);

🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests.
📄 Licença

Este projeto é open-source e está sob a licença MIT.
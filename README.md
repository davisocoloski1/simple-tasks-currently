# ✅ Simple Tasks

A simple tasks manager made with python, using PostgreSQL as dada persistence

## 📁 Project Structure

```bash
simple_tasks/   
        ├── main.py 
        ├── src/ │ 
            └── tasks.py # TaskManager class with all the database logic
        ├── utils/ │ 
            └── clear.py # Class/function to clear the terminal 
        ├── .env # Environment variables (DO NOT COMMIT)
        ├── .gitignore 
        ├── requirements.txt 
        └── README.md
```


## 🚀 Features

- ✅ Adding tasks
- 📋 List tasks
- 🔄 Status changing (`Active`, `Inactive`, `Completed`)
- 🗑️ Delete tasks

## ⚙️ Requirements

- Python 3.10+
- PostgreSQL
    - Locally installed
    - Needs pgAdmin 4
- Library `psycopg2`
- Library `python-dotenv`

Download the requirements using:

```bash
pip install -r requirements.txt
```

🔐 Environment variables

Create a .env file in the project root with the following content:

```bash
DB_NAME=simple_tasks
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

⚠️ Never commit the .env file. It is already listed in .gitignore
```
🛠️ Usage

In the terminal:

```bash
python main.py
```
🗃️ Database

Make sure you create the simple_tasks table in your PostgreSQL database with:

```bash
CREATE TABLE simple_tasks (
    id SERIAL PRIMARY KEY,
    to_do TEXT NOT NULL,
    status TEXT NOT NULL,
    entry_time TEXT
);
```

🤝 Contribution

Feel free to open issues or pull requests
📄 License

This project is open-source and is licensed under the MIT license.
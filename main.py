from sqlalchemy.schema import CreateTable
from app.models import User, Task
from app.backend.db import engine, create_db

# Создание таблиц в базе данных
create_db()

# Распечатка SQL-запросов для создания таблиц
print("SQL для User:", CreateTable(User.__table__).compile(engine))
print("SQL для Task:", CreateTable(Task.__table__).compile(engine))
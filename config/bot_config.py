import os
import sqlite3
from pathlib import Path

from dotenv import dotenv_values

# Настройки можно передать переменными окружения или через config/.env.
config = dotenv_values("./config/.env")

API_TOKEN = os.getenv("API_TOKEN") or config["API_TOKEN"]
ADMIN = int(os.getenv("ADMIN") or config["ADMIN"])

# Путь к SQLite настраивается переменной DATABASE_PATH, чтобы в Docker
# хранить базу в примонтированном volume и не терять данные при пересборке.
database_path = Path(os.getenv("DATABASE_PATH", "utils/database.db"))
database_path.parent.mkdir(parents=True, exist_ok=True)

DB = sqlite3.connect(database_path)
DB.row_factory = sqlite3.Row

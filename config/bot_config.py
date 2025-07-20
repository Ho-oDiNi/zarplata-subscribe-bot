from dotenv import dotenv_values
import sqlite3

# Получение токена из файла .env
config = dotenv_values("./config/.env")
API_TOKEN = config["API_TOKEN"]
ADMIN = int(config["ADMIN"])

# Подключение к базе данных MySQL
DB = sqlite3.connect("utils/database.db")
DB.row_factory = sqlite3.Row
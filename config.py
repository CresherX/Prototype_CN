import os
from dotenv import load_dotenv

# Загрузка .env только локально
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "mydb"),
}

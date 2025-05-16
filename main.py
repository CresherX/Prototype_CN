from flask import Flask
from flask_cors import CORS
from app.db import init_db
from app.route import routes

app = Flask(__name__)
CORS(app)

# Инициализация базы данных
init_db()

# Регистрируем Blueprint
app.register_blueprint(routes, url_prefix="/api")

# Роут для парсинга
@app.route("/parse", methods=["GET"])
def trigger_parse():
    from app.parser import parse_articles  
    parse_articles()  # вызовт parse_articles
    return "Парсинг выполнен", 200

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)

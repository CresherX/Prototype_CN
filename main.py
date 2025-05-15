from flask import Flask
from app.db import init_db
from app.route import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

init_db()
@app.route("/parse", methods=["GET"])
def trigger_parse():
    from app.parser import parse_articles  
    parse_articles()  # вызывает insert_article
    return "Парсинг выполнен", 200
# Регистрация Blueprint без префикса
app.register_blueprint(routes, url_prefix="/api")
if __name__ == "__main__":
    app.run(debug=True)

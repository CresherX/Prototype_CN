# main.py
from flask import Flask
from app.db import init_db
from app.route import routes

app = Flask(__name__)
init_db()

# Регистрируем Blueprint без префикса
app.register_blueprint(routes, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Конфигурация из config.py
    import os
    app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'))

    # Регистрация маршрутов
    from .route import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

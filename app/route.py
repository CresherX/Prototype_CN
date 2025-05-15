from flask import Blueprint, jsonify
from app.db import get_all_articles, get_articles_by_source, fetch_latest_articles_from_db  # убедись, что эти функции есть

routes = Blueprint('routes', __name__)

@routes.route('/articles', methods=['GET'])
def all_articles():
    articles = get_all_articles()
    return jsonify(articles), 200

@routes.route('/articles/<source>', methods=['GET'])
def articles_by_source(source):
    articles = get_articles_by_source(source)
    return jsonify(articles), 200

@routes.route('/articles/latest/<int:count>', methods=['GET'])
def get_latest_articles(count):
    articles = fetch_latest_articles_from_db(count)
    return jsonify(articles), 200

@routes.route('/')
def home():
    return "Главная страница"

from flask import Blueprint, jsonify
from app.db import get_all_articles, get_articles_by_source

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
def latest_articles(count):
    articles = get_all_articles()[:count]  # Предполагается, что они уже отсортированы
    return jsonify(articles), 200
@routes.route('/')
def home():
    return "Главная страница"

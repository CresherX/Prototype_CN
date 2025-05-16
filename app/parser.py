import requests
from bs4 import BeautifulSoup
from app.db import insert_article

def parse_rbc():
    url = 'https://www.rbc.ru/crypto/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='item__link')
    result = []

    for article in articles:
        title = article.get_text(strip=True)
        link = article['href']
        source = 'RBC'
        insert_article(title, link, source, None)
        print(f"Insert Article: {title}, {link}, {source}, ")
        result.append({
            'title': title,
            'url': link,
            'description': None
        })
    return result

if __name__ == "__main__":
    # Пример работы с каждым парсером
    sources = {
        "RBC": parse_rbc()
    }

    # Перебираем все парсеры и выводим результаты
    for source, articles in sources.items():
        print(f"--- {source} ---")
        for article in articles:
            print(f"Заголовок: {article['title']}")
            print(f"Ссылка: {article['url']}")
            print(f"Описание: {article.get('description', 'Нет описания')}")
            print("-" * 40)
def parse_articles():
    parse_rbc()

import requests
from bs4 import BeautifulSoup
from app.db import insert_article

def parse_cryptonews():
    url = 'https://cryptonews.net/ru/news/'
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'ru-RU,ru;q=0.9',
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Ошибка при загрузке Cryptonews: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('div.article__item')  # Обновлённый селектор
    result = []

    for article in articles:
        a_tag = article.find('a', class_='article__title')
        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = "https://cryptonews.net" + a_tag['href']
        source = 'Cryptonews'

        insert_article(title, link, source, None)
        print(f"Insert Article: {title}, {link}, {source}")
        result.append({
            'title': title,
            'url': link,
            'description': None
        })

    return result


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
        "Cryptonews": parse_cryptonews(),
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
    parse_cryptonews()
    parse_rbc()

import mysql.connector
from parser.config import DB_CONFIG

def init_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                url VARCHAR(255),
                source VARCHAR(100),
                description TEXT
            )
        """)

        connection.commit()
        print("Database initialized successfully.")

    except mysql.connector.Error as err:
        print(f"MySQL Error during DB initialization: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Получение всех статей
def get_all_articles():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM articles ORDER BY id DESC")
        results = cursor.fetchall()

        return results

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Получение статей по источнику
def get_articles_by_source(source):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM articles WHERE source = %s ORDER BY id DESC"
        cursor.execute(query, (source,))
        results = cursor.fetchall()

        return results

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
# Вставка статьи

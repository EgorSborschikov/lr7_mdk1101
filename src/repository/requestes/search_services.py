import sys
import os
import psycopg2
from psycopg2 import sql

# Добавляем путь к корневой директории проекта в PYTHONPATH

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from config.config import db_params_config

# Параметры подключения к базе данных
db_params = db_params_config

# Часть слова, которую ищем
part_of_word = 'Строительство'

# Подключение к базе данных
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Выполнение запроса
query = sql.SQL("SELECT name FROM services WHERE name LIKE %s")
cursor.execute(query, ('%' + part_of_word + '%'))

# Получение результатов
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие курсора и соединения
cursor.close()
conn.close()

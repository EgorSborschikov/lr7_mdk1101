import psycopg2
from psycopg2 import sql
import sys
import os
from tabulate import tabulate

# Добавляем путь к корневой директории проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from config.config import db_params_config
from schema.models import Order, OrderStatus, Prices, Service, ServiceType, User

# Параметры подключения к базе данных
db_params = db_params_config

# Подключение к базе данных
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Выполнение запроса
query = sql.SQL("""
    SELECT
        o.id AS order_id,
        u.last_name AS user_last_name,
        u.first_name AS user_first_name,
        u.middle_name AS user_middle_name,
        s.name AS service_name,
        st.name AS service_type_name,
        p.price AS service_price,
        os.name AS order_status
    FROM
        orders o
    JOIN
        users u ON o.user_id = u.id
    JOIN
        services s ON o.service_id = s.id
    JOIN
        service_types st ON s.service_type_id = st.id
    JOIN
        prices p ON s.id = o.service_id
    JOIN
        order_statuses os ON o.status_id = os.id;
""")

# Выполнение запроса
cursor.execute(query)

# Получение результатов
results = cursor.fetchall()

# Закрытие курсора и соединения
cursor.close()
conn.close()

# Вывод результатов в виде таблицы
if results:
    # Получение имен столбцов
    column_names = [desc[0] for desc in cursor.description]
    # Вывод таблицы
    print(tabulate(results, headers=column_names, tablefmt="grid"))
else:
    print("Нет результатов для отображения.")

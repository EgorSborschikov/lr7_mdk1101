import sys
import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Добавляем путь к корневой директории проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.schema.models import Base, User, Service, Order, UserType, Gender, Territory, Settlement, ServiceType, OrderStatus, JWTToken, Prices
from src.config.config import config_uri

# Создание подключения к базе данных
engine = create_engine(config_uri)
Session = sessionmaker(bind=engine)
session = Session()

# Функция для добавления данных, если они не существуют
def add_if_not_exists(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if not instance:
        instance = model(**kwargs)
        session.add(instance)
    return instance

# Создание типов пользователей
user_types = [
    add_if_not_exists(session, UserType, name='Физическое лицо'),
    add_if_not_exists(session, UserType, name='Юридическое лицо'),
    add_if_not_exists(session, UserType, name='Администратор')
]
session.commit()

# Создание полов
genders = [
    add_if_not_exists(session, Gender, name='Мужской'),
    add_if_not_exists(session, Gender, name='Женский')
]
session.commit()

# Создание территорий
territories = [
    add_if_not_exists(session, Territory, name='Москва'),
    add_if_not_exists(session, Territory, name='Санкт-Петербург'),
    add_if_not_exists(session, Territory, name='Новосибирск'),
    add_if_not_exists(session, Territory, name='Екатеринбург'),
    add_if_not_exists(session, Territory, name='Казань')
]
session.commit()

# Создание населенных пунктов
settlements = [
    add_if_not_exists(session, Settlement, name='Москва', territory=territories[0]),
    add_if_not_exists(session, Settlement, name='Санкт-Петербург', territory=territories[1]),
    add_if_not_exists(session, Settlement, name='Новосибирск', territory=territories[2]),
    add_if_not_exists(session, Settlement, name='Екатеринбург', territory=territories[3]),
    add_if_not_exists(session, Settlement, name='Казань', territory=territories[4]),
    add_if_not_exists(session, Settlement, name='Подольск', territory=territories[0]),
    add_if_not_exists(session, Settlement, name='Колпино', territory=territories[1]),
    add_if_not_exists(session, Settlement, name='Бердск', territory=territories[2]),
    add_if_not_exists(session, Settlement, name='Верхняя Пышма', territory=territories[3]),
    add_if_not_exists(session, Settlement, name='Зеленодольск', territory=territories[4])
]
session.commit()

# Создание типов услуг
service_types = [
    add_if_not_exists(session, ServiceType, name='Строительство частных домов'),
    add_if_not_exists(session, ServiceType, name='Строительство многоэтажных жилых домов'),
    add_if_not_exists(session, ServiceType, name='Отделка помещений'),
    add_if_not_exists(session, ServiceType, name='Коммунальное строительство')
]
session.commit()

# Создание услуг
services = [
    add_if_not_exists(session, Service, name='Строительство частного дома', description='Строительство частных домов', service_type=service_types[0]),
    add_if_not_exists(session, Service, name='Строительство многоэтажного жилого дома', description='Строительство многоэтажных жилых домов', service_type=service_types[1]),
    add_if_not_exists(session, Service, name='Отделка квартиры', description='Отделка квартир', service_type=service_types[2]),
    add_if_not_exists(session, Service, name='Строительство детской площадки', description='Строительство детских площадок', service_type=service_types[3]),
    add_if_not_exists(session, Service, name='Строительство парка', description='Строительство парков', service_type=service_types[3]),
    add_if_not_exists(session, Service, name='Строительство автомобильной дороги', description='Строительство автомобильных дорог', service_type=service_types[3]),
    add_if_not_exists(session, Service, name='Строительство железной дороги', description='Строительство железных дорог', service_type=service_types[3]),
    add_if_not_exists(session, Service, name='Строительство культурного центра', description='Строительство культурных центров', service_type=service_types[3]),
    add_if_not_exists(session, Service, name='Строительство спортивного комплекса', description='Строительство спортивных комплексов', service_type=service_types[3]),
    add_if_not_exists(session, Service, name='Строительство торгового центра', description='Строительство торговых центров', service_type=service_types[3])
]
session.commit()

# Создание центров
prices = [
    add_if_not_exists(session, Prices, price = '1000000', service=services[0]),
    add_if_not_exists(session, Prices, price = '15000000', service=services[1]),
    add_if_not_exists(session, Prices, price = '150000', service=services[2]),
    add_if_not_exists(session, Prices, price = '20000000', service=services[3]),
]
session.commit()

# Создание статусов заказов
order_statuses = [
    add_if_not_exists(session, OrderStatus, name='В ожидании'),
    add_if_not_exists(session, OrderStatus, name='В процессе'),
    add_if_not_exists(session, OrderStatus, name='Завершен')
]
session.commit()

# Создание JWT токенов
jwt_tokens = [
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'),
    add_if_not_exists(session, JWTToken, token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c')
]
session.commit()

# Создание пользователей
users = [
    add_if_not_exists(session, User, last_name='Иванов', first_name='Иван', middle_name='Иванович', gender=genders[0], birth_date=datetime.date(1990, 1, 1), user_type=user_types[0], territory=territories[0], settlement=settlements[0], jwt=jwt_tokens[0], email='ivanov@example.com'),
    add_if_not_exists(session, User, last_name='Петров', first_name='Петр', middle_name='Петрович', gender=genders[0], birth_date=datetime.date(1985, 5, 15), user_type=user_types[1], organization_name='ООО "Петров"', territory=territories[1], settlement=settlements[1], jwt=jwt_tokens[1], email='petrov@example.com'),
    add_if_not_exists(session, User, last_name='Сидоров', first_name='Сергей', middle_name='Сергеевич', gender=genders[0], birth_date=datetime.date(1980, 8, 20), user_type=user_types[0], territory=territories[2], settlement=settlements[2], jwt=jwt_tokens[2], email='sidorov@example.com'),
    add_if_not_exists(session, User, last_name='Кузнецов', first_name='Кузьма', middle_name='Кузьмич', gender=genders[0], birth_date=datetime.date(1975, 12, 10), user_type=user_types[1], organization_name='ООО "Кузнецов"', territory=territories[3], settlement=settlements[3], jwt=jwt_tokens[3], email='kuznetsov@example.com'),
    add_if_not_exists(session, User, last_name='Смирнов', first_name='Семён', middle_name='Семенович', gender=genders[0], birth_date=datetime.date(1992, 3, 5), user_type=user_types[0], territory=territories[4], settlement=settlements[4], jwt=jwt_tokens[4], email='smirnov@example.com'),
    add_if_not_exists(session, User, last_name='Васильев', first_name='Василий', middle_name='Васильевич', gender=genders[0], birth_date=datetime.date(1988, 7, 25), user_type=user_types[1], organization_name='ООО "Васильев"', territory=territories[0], settlement=settlements[5], jwt=jwt_tokens[5], email='vasilyev@example.com'),
    add_if_not_exists(session, User, last_name='Попов', first_name='Пётр', middle_name='Петрович', gender=genders[0], birth_date=datetime.date(1995, 11, 30), user_type=user_types[0], territory=territories[1], settlement=settlements[6], jwt=jwt_tokens[6], email='popov@example.com'),
    add_if_not_exists(session, User, last_name='Соколов', first_name='Савелий', middle_name='Савельевич', gender=genders[0], birth_date=datetime.date(1983, 4, 18), user_type=user_types[1], organization_name='ООО "Соколов"', territory=territories[2], settlement=settlements[7], jwt=jwt_tokens[7], email='sokolov@example.com'),
    add_if_not_exists(session, User, last_name='Михайлов', first_name='Михаил', middle_name='Михайлович', gender=genders[0], birth_date=datetime.date(1991, 6, 9), user_type=user_types[0], territory=territories[3], settlement=settlements[8], jwt=jwt_tokens[8], email='mikhailov@example.com'),
    add_if_not_exists(session, User, last_name='Новиков', first_name='Николай', middle_name='Николаевич', gender=genders[0], birth_date=datetime.date(1987, 9, 22), user_type=user_types[1], organization_name='ООО "Новиков"', territory=territories[4], settlement=settlements[9], jwt=jwt_tokens[9], email='novikov@example.com')
]
session.commit()

# Создание заказов
orders = [
    add_if_not_exists(session, Order, user=users[0], service=services[0], status=order_statuses[0]),
    add_if_not_exists(session, Order, user=users[1], service=services[1], status=order_statuses[1]),
    add_if_not_exists(session, Order, user=users[2], service=services[2], status=order_statuses[2]),
    add_if_not_exists(session, Order, user=users[3], service=services[3], status=order_statuses[0]),
    add_if_not_exists(session, Order, user=users[4], service=services[4], status=order_statuses[1]),
    add_if_not_exists(session, Order, user=users[5], service=services[5], status=order_statuses[2]),
    add_if_not_exists(session, Order, user=users[6], service=services[6], status=order_statuses[0]),
    add_if_not_exists(session, Order, user=users[7], service=services[7], status=order_statuses[1]),
    add_if_not_exists(session, Order, user=users[8], service=services[8], status=order_statuses[2]),
    add_if_not_exists(session, Order, user=users[9], service=services[9], status=order_statuses[0])
]
session.commit()

from sqlalchemy import Column, String, Date, Integer, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID, MONEY
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UserType(Base):
    __tablename__ = 'user_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class Gender(Base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class Territory(Base):
    __tablename__ = 'territories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class Settlement(Base):
    __tablename__ = 'settlements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    territory_id = Column(Integer, ForeignKey('territories.id'), nullable=False)
    territory = relationship('Territory', back_populates='settlements')

Territory.settlements = relationship('Settlement', order_by=Settlement.id, back_populates='territory')

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    gender_id = Column(Integer, ForeignKey('genders.id'), nullable=False)
    birth_date = Column(Date, nullable=False)
    user_type_id = Column(Integer, ForeignKey('user_types.id'), nullable=False)
    organization_name = Column(String, nullable=True)
    territory_id = Column(Integer, ForeignKey('territories.id'), nullable=False)
    settlement_id = Column(Integer, ForeignKey('settlements.id'), nullable=False)
    jwt_id = Column(Integer, ForeignKey('jwt_tokens.id'), nullable=False)
    email = Column(String, nullable=False, unique=True)  # Новое поле для электронной почты
    gender = relationship('Gender')
    user_type = relationship('UserType')
    territory = relationship('Territory')
    settlement = relationship('Settlement')
    jwt = relationship('JWTToken')

class ServiceType(Base):
    __tablename__ = 'service_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class Service(Base):
    __tablename__ = 'services'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    service_type_id = Column(Integer, ForeignKey('service_types.id'), nullable=False)
    service_type = relationship('ServiceType')

class Prices(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(MONEY)
    service_id = Column(UUID(as_uuid=True), ForeignKey('services.id'), nullable=False)
    service = relationship('Service', back_populates='centers')

Service.centers = relationship('Center', order_by=Prices.id, back_populates='service')

class OrderStatus(Base):
    __tablename__ = 'order_statuses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    service_id = Column(UUID(as_uuid=True), ForeignKey('services.id'), nullable=False)
    status_id = Column(Integer, ForeignKey('order_statuses.id'), nullable=False)
    user = relationship('User', back_populates='orders')
    service = relationship('Service', back_populates='orders')
    status = relationship('OrderStatus')

User.orders = relationship('Order', order_by=Order.id, back_populates='user')
Service.orders = relationship('Order', order_by=Order.id, back_populates='service')

class JWTToken(Base):
    __tablename__ = 'jwt_tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, nullable=False, unique=True)

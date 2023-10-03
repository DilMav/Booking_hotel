from sqlalchemy import JSON, Column, BigInteger, Integer, String, Float, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy import Computed

from database import Base
from datetime import datetime


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    profile_photo = Column(String, default='None')
    city = Column(String)

    reg_date = Column(DateTime)

    user_fk = relationship('Booking', lazy='subquery')

    def __str__(self):
        return f'Пользователь: id - {self.id}, email - {self.email}'


# Таблица отелей
class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=150), nullable=False)
    location = Column(String(length=300), nullable=False)
    services = Column(JSON, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)

    image_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user_fk = relationship(User, lazy='subquery')

    def __str__(self):
        return f'Отель: id - {self.id}, название - {self.name}'


# Таблица номеров
class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=500), nullable=True)
    price_per_day = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)

    hotel_id = Column(ForeignKey('hotels.id'))
    image_id = Column(Integer, nullable=False)

    reg_date = Column(DateTime)

    hotel_fk = relationship('Hotel', lazy='subquery')
    booking_fk = relationship('Booking', lazy='subquery')

    def __str__(self):
        return f'Номер: id - {self.id}, название - {self.name}'


# Таблица бронирования
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price_per_day = Column(Integer, nullable=False)
    total_days = Column(Integer, Computed('date_to - date_from'), nullable=False)
    total_cost = Column(Integer, Computed('(date_to - date_from) * price_per_day'), nullable=False)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))

    user_fk = relationship('User', lazy='subquery', overlaps="user_fk")
    room_fk = relationship('Room',  lazy='subquery', overlaps="booking_fk")

    def __str__(self):
        return f'Бронирование: id - {self.id}, c {self.date_from} по {self.date_to}'


# Заблокированные пользователи
class BlockedUser(Base):
    __tablename__ = 'blocklist'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    blocked_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

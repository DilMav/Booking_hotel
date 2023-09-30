from datetime import datetime
from pydantic import BaseModel


# Модель отображения бронирования
class RegisterBookingModel(BaseModel):
    id: int
    date_from: date
    date_to: date
    price_per_day: int
    total_days: int
    total_cost: int
    booking_id: int
    room_id: int
    user_id: int


# Модель отображения бронирования пользователя
class BookingUserModel(BaseModel):
    id: int
    name: str
    description: str
    services: str
    date_from: date
    date_to: date
    price_per_day: int
    total_days: int
    total_cost: int
    user_id: int
    room_id: int
    image_id: str



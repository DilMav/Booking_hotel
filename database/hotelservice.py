from datetime import datetime

from database import get_db
from database.models import Hotel

from hotel import RegisterHotelModel


# Добавить отель
def add_new_hotel_db(hotel_data: RegisterHotelModel):
    db = next(get_db())

    hotel_info = hotel_data.model_dump()

    new_hotel = Hotel(reg_date=datetime.now(), **hotel_info)

    db.add(new_hotel)
    db.commit()

    return True


# Удалить определённый отель
def delete_exact_hotel_db(user_id: int, hotel_id: str):
    db = next(get_db())

    exact_hotel = db.query(Hotel).filter_by(user_id=user_id, id=hotel_id).first()

    if exact_hotel:
        db.delete(exact_hotel)
        db.commit()

        return 'Отель успешно удален'

    return 'Отель не найден'


# Вывести все отели пользователя
def get_all_user_hotels_db(user_id: int):
    db = next(get_db())

    all_hotels = db.query(Hotel).filter_by(user_id=user_id).all()

    return all_hotels


# Вывести определённый отель пользователя
def get_exact_user_hotel_db(user_id: int, hotel_id: int):
    db = next(get_db())

    exact_hotel = db.query(Hotel).filter_by(user_id=user_id, hotel_id=hotel_id, id=room_id).first()

    return exact_hotel

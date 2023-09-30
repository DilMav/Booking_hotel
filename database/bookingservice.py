from datetime import datetime

from database import get_db
from database.models import Booking

from booking import RegisterBookingModel


# Добавить бронирование
def add_new_booking_db(booking_data: RegisterBookingModel):
    db = next(get_db())

    booking_info = booking_data.model_dump()

    new_booking = Hotel(reg_date=datetime.now(), **hotel_info)

    db.add(new_booking)
    db.commit()

    return True


# Удалить определённое бронирование
def delete_exact_booking_db(user_id: int, booking_id: str):
    db = next(get_db())

    exact_booking = db.query(Booking).filter_by(user_id=user_id, id=booking_id).first()

    if exact_booking:
        db.delete(exact_booking)
        db.commit()

        return 'Бронирование успешно удалено'

    return 'Бронь не найдена'


# Вывести все бронирования пользователя
def get_all_user_bookings_db(user_id: int):
    db = next(get_db())

    all_bookings = db.query(Booking).filter_by(user_id=user_id).all()

    return all_bookings


# Вывести определённое бронирование пользователя
def get_exact_user_booking_db(user_id: int, booking_id: int):
    db = next(get_db())

    exact_booking = db.query(Booking).filter_by(booking_id=booking_id,
                                                user_id=user_id,
                                                hotel_id=hotel_id,
                                                id=room_id).first()

    return exact_booking

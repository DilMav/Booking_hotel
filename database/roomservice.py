from datetime import datetime

from database import get_db
from database.models import Room, Hotel
from room import RegisterRoomModel


# Добавить комнату
def add_new_room_db(room_data: RegisterRoomModel):
    db = next(get_db())

    room_info = room_data.model_dump()

    new_room = Room(reg_date=datetime.now(), **room_info)

    db.add(new_room)
    db.commit()

    return True


# Удалить определённую комнату
def delete_exact_room_db(user_id: int, room_id: int):
    db = next(get_db())

    exact_room = db.query(Room).filter_by(user_id=user_id, id=room_id).first()

    if exact_room:
        db.delete(exact_room)
        db.commit()

        return 'Номер успешно удален'

    return 'Номер не найден'


# Вывести все номера пользователя
def get_all_user_rooms_db(user_id: int):
    db = next(get_db())

    exact_room = db.query(Room).filter_by(user_id=user_id).all()

    return exact_room


# Вывести определённый номер пользователя
def get_exact_user_room_db(user_id: int, hotel_id: int):
    db = next(get_db())

    exact_room = db.query(Room).filter_by(user_id=user_id, id=hotel_id).first()

    return exact_room

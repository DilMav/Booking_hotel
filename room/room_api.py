from fastapi import APIRouter

from room import RegisterRoomModel
from database.roomservice import \
    get_exact_user_room_db, \
    get_all_user_rooms_db,\
    add_new_room_db

room_router = APIRouter(prefix='/room', tags=['Работа с номерами'])


# Добавить номер пользователя
@room_router.post('/add-room')
async def add_new_room(data: RegisterRoomModel):
    try:
        result = add_new_room_db(data)

        return {'status': 1, 'data': result}

    except Exception as error:
        return {'status': 0, 'data': str(error)}


# Удалить номер пользователя
@room_router.delete('/delete-room')
async def delete_exact_room(user_id: int, room_id: int):
    result = delete_exact_room_db(user_id, room_id)

    return {'status': 1, 'data': result}


# Вывести все номера определённого пользователя
@room_router.get('/get-all-user-rooms')
async def get_all_rooms(user_id: int):
    result = get_all_user_rooms_db(user_id)

    return {'status': 1, 'data': result}


# Вывести номер определённой отеля
@room_router.get('/get-exact-room')
async def get_exact_room(user_id: int, room_id: int):
    result = get_exact_user_room_db(user_id, room_id)

    return {'status': 1, 'data': result}

from fastapi import APIRouter


from hotel import RegisterHotelModel
from database.hotelservice import \
    get_all_user_hotels_db, \
    get_exact_user_hotel_db, \
    add_new_hotel_db, \
    delete_exact_hotel_db


hotel_router = APIRouter(prefix='/hotel', tags=['Работа с отелями'])


# Добавить отель пользователя
@hotel_router.post('/add-hotel')
async def add_new_hotel(data: RegisterHotelModel):
    try:
        result = add_new_hotel_db(data)

        return {'status': 1, 'data': result}

    except Exception as error:
        return {'status': 0, 'data': str(error)}


# Удалить отель пользователя
@hotel_router.delete('/delete-hotel')
async def delete_exact_hotel(user_id: int, hotel_id: str):
    result = delete_exact_hotel_db(user_id, hotel_id)

    return {'status': 1, 'data': result}


#  Вывод всех отелей пользователя
@hotel_router.get('/get-all-user-hotels')
async def get_all_hotels(user_id: int):
    result = get_all_user_hotels_db(user_id)

    return {'status': 1, 'data': result}


# Вывод определённого отеля пользователя
@hotel_router.get('/get-exact-hotel')
async def get_exact_hotel(user_id: int, hotel_id: int):
    result = get_exact_user_hotel_db(user_id, hotel_id)
    return {'status': 1, 'data': result}

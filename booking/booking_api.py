from fastapi import APIRouter

from booking import RegisterBookingModel
from database.bookingservice import \
    get_all_user_bookings_db, \
    get_exact_user_booking_db, \
    add_new_booking_db, \
    delete_exact_booking_db

booking_router = APIRouter(prefix='/bookings', tags=['Работа с бронированиями'])


# Добавить бронирование
@booking_router.post('/add-booking')
async def add_new_booking(data: RegisterBookingModel):
    try:
        result = add_new_booking_db(data)

        return {'status': 1, 'data': result}

    except Exception as error:
        return {'status': 0, 'data': str(error)}


# Удалить бронирование пользователя
@booking_router.delete('/delete-booking')
async def delete_exact_booking(user_id: int, booking_id: int):
    result = delete_exact_booking_db(user_id, booking_id)
    return {'status': 1, 'data': result}


# Вывод всех бронирований пользователя
@booking_router.get('/get-all-user-bookings')
async def get_all_bookings(user_id: int):
    result = get_all_user_bookings_db(user_id)

    return {'status': 1, 'data': result}


# Вывод определённого бронирования пользователя
@booking_router.get('/get-exact-booking')
async def get_exact_booking(user_id: int, booking_id: int):
    result = get_exact_user_booking_db(user_id, booking_id)
    return {'status': 1, 'data': result}

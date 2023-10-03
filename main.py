from fastapi import FastAPI

from booking.booking_api import booking_router
from hotel.hotel_api import hotel_router
from room.room_api import room_router
from user.user_api import user_router


# Создать все таблицы
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Регистрация компонентов
app.include_router(booking_router)
app.include_router(hotel_router)
app.include_router(room_router)
app.include_router(user_router)


@app.get('/home')
async def hello():
    return{'message': 'Hello'}

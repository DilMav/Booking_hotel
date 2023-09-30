from fastapi import FastAPI

from hotel.hotel_api import card_router
from user.user_api import user_router
from room.room_api import transaction_router

# Создать все таблицы
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Регистрация компонентов
app.include_router(user_router)
app.include_router(card_router)
app.include_router(transaction_router)


@app.get('/home')
async def hello():
    return{'message': 'Hello'}

from pydantic import BaseModel


# Модель отображения комнаты

class RegisterRoomModel(BaseModel):
    id: int
    name: str
    description: str
    price_per_day: int
    services: str
    quantity: int
    hotel_id: int
    image_id: int

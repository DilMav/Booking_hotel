from pydantic import BaseModel


# Модель отображения отеля
class RegisterHotelModel(BaseModel):
    id: int
    name: str
    location: str
    services: str
    rooms_quantity: int
    image_id: int


# Модель отображения всех комнат отеля
class HotelRoomsModel(BaseModel):
    id: int
    name: str
    description: str
    price_per_day: int
    services: str
    quantity: int
    available_rooms: int
    preliminary_cost: int
    image_id: int

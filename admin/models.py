from admin import ModelView

from models import Booking
from models import Hotel
from models import Room
from models import User


# Для отображения пользователей в админке
class UserAdmin(ModelView, model=User):

    column_list = [User.id, User.email, User.booking]
    column_details_exclude_list = [User.password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"


# Для отображения отелей в админке
class HotelAdmin(ModelView, model=Hotel):

    column_list = [c.name for c in Hotel.__table__.c]
    column_list += [Hotel.rooms]
    name = "Отель"
    name_plural = "Отели"


# Для отображения комнат отелей в админке
class RoomAdmin(ModelView, model=Room):

    column_list = [c.name for c in Room.__table__.c]
    column_list += [Room.hotel, Room.booking]
    name = "Номер"
    name_plural = "Номера"


# Для отображения бронирований в админке
class BookingAdmin(ModelView, model=Booking):

    column_list = [c.name for c in Booking.__table__.c]
    column_list += [Booking.user]
    name = "Бронирование"
    name_plural = "Бронирования"

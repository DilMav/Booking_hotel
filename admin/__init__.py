from pydantic import BaseModel


# Валидатор для входа в аккаунт
class LoginAdminModel(BaseModel):
    email: str
    password: int


# Валидатор регистрации пользователя
class RegisterUserModel(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str
    password: str

from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str


class ReturnUser(BaseUser):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserCreation(BaseUser):
    password:int
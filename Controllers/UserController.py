from fastapi import APIRouter
from ReturnObjects import User
from Managers.UserManager import UserManager
from fastapi_sqlalchemy import db

router = APIRouter(prefix="/users", tags=["Users"])
Manager = UserManager(db)


@router.get("/users/{id}", response_model=User.ReturnUser)
def GetUser(id: int):
    user = Manager.GetUser(id)
    return user

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy.ext.declarative import declarative_base
from fastapi_sqlalchemy import db
from ReturnObjects.User import ReturnUser


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="")

Base = declarative_base()


@app.get("/")
def Home():
    return {"ServerStatus": True}


@app.get("/users", response_model=ReturnUser)
def User():
    from Models import User
    user = db.session.query(User.User).first()

    return user

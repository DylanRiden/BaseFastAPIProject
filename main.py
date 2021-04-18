from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy.middleware import DBSessionMeta
from sqlalchemy.ext.declarative import declarative_base
from fastapi_sqlalchemy import db


def EnableRouters(db: DBSessionMeta):
    from Controllers import UserController
    routers = []
    routers.append(UserController.router)
    UserController.db = db
    return routers


app = FastAPI()
Base = declarative_base()
app.add_middleware(DBSessionMiddleware, db_url="")

for i in EnableRouters(db):
    app.include_router(i)


@app.get("/")
def Home():
    return {"ServerStatus": "Running"}

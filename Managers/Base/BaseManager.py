from fastapi_sqlalchemy.middleware import DBSessionMeta


# Base Class For DataManager
class BaseManager:
    def __init__(self, db: DBSessionMeta):
        self.db = db

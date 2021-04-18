from Managers.Base.BaseManager import BaseManager
from Models.User import User


class UserManager(BaseManager):

    def GetUser(self,id: int):
        userQuery = User
        userQuery.id = id
        user = self.db.session.query(userQuery).first()
        return user

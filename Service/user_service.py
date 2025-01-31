"""This Service helps to signup users and login users"""
from datetime import datetime
from Data import Users
from Repository import UserRepository
from .encryptor import EncryptionService


class UserService():
    """Services like login and signup"""

    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo
        self.logged_in = False
        self.user_id = None
        self.user_secret_key = None

    def login(self, username: str, password: str):
        """Login method"""
        # if all user already in db
        users = self.user_repo.get_users()
        for user in users:
            if username == user.user_name and user.password == password:
                self.logged_in = True
                self.user_id = user.user_id
                self.user_secret_key = user.secret_key
        return self.logged_in

    def logout(self):
        raise NotImplementedError

    def signup(self, user_info: dict):
        # generate secret key
        enc = EncryptionService()
        generated__secret_key = enc.get_key().decode()
        user = Users(
            user_id= None,
            user_name=user_info.get("user_name"),
            password=user_info.get("password"),
            secret_key=generated__secret_key,
            created_at=datetime.today().isoformat()
        )
        saved_user = self.user_repo.save_user(user)
        return saved_user

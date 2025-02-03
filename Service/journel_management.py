"""JOURNEL MANAGEMENT"""
from Repository import JournelRepo
from .user_service import UserService


class JournelManagement():

    def __init__(self, journel_repo: JournelRepo, user_service: UserService):
        self.journel_repo = journel_repo
        self.user_service = user_service

    def create_new_journel(self, journel_data: dict):
        pass

    def get_all_user_journel(self):
        journels = self.journel_repo.get_all_journel(self.user_service.user_id)
        return journels
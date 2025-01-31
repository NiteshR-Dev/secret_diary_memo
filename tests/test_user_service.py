import unittest
from Data.data import Users
from Repository import UserRepository
from Service import UserService
from datetime import datetime

from unittest.mock import Mock, patch,MagicMock


wednesday = datetime(year=2025, month=1, day=1)
sunday = datetime(year=2025, month=1, day=5)

USERS = [Users(user_id=1,
               user_name="Gopal",
               password="password",
               secret_key="ABC",
               created_at=sunday.isoformat()
               )]


def get_users():
    return USERS


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.USERS = [Users(user_id=1,
                           user_name="Gopal",
                           password="password",
                           secret_key="ABC",
                           created_at=sunday.isoformat()
                           )]

    def setUp(self):
        self.patcher = patch("Repository.UserRepository")
        self.mock_user_repo = self.patcher.start()
        self.mock_user_repo.get_users.return_value = get_users()
        self.mock_user_repo.save_user = lambda data : self.save_user(data)

    def tearDown(self):
        self.patcher.stop()

    def save_user(self,user: Users):
        if not user.user_id:
            user.user_id = len(self.USERS)
        self.USERS.append(user)
        return self.USERS.pop()

    def test_user_login(self):
        self.user_service = UserService(self.mock_user_repo)
        user_name_parameter = "Gopal"
        user_password_parameter = "password"
        actual_response = self.user_service.login(
            username=user_name_parameter, password=user_password_parameter)
        self.assertEqual(actual_response, True)
        self.assertEqual(self.user_service.logged_in, True)
        self.assertEqual(self.user_service.user_id, 1)

    @patch("Service.user_service.EncryptionService")
    def test_sign_up(self, mock_encryption_service ):
        mock_object  =  MagicMock()
        # mock_encryption_service.get_key.side_effect = "ABC"
        mock_encryption_service.return_value = mock_object
        mock_object.get_key.return_value = b'ABC'
        self.user_service = UserService(self.mock_user_repo)
        user_info = {
            "user_name": "Nitesh",
            "password": "password1"
        }
        actual_response = self.user_service.signup(user_info)
        expected_response = Users(
            user_id=1,
            user_name="Nitesh",
            password="password1",
            secret_key="ABC",
            created_at=datetime.today().isoformat()
        )
        self.assertEqual(actual_response,expected_response)

        # a new user must be registered in db


if __name__ == "__main__":
    unittest.main()

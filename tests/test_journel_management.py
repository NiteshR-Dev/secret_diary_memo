from unittest import TestCase
from unittest.mock import patch
from datetime import datetime
from Data import Journel
from Service import JournelManagement

SUNDAY = datetime(year=2025, month=1, day=5)


class MockedUserService():
    def __init__(self):
        self.user_id = 1


class TestJournelManagement(TestCase):
    JOURNELS = [
        Journel(
            journel_id=1,
            user_id=1,
            title="TEST",
            description="THIS IS A TEST",
            created_at=SUNDAY.isoformat(),
            modified_at=SUNDAY.isoformat()
        )
    ]

    def setUp(self):
        self.patcher = patch("Repository.JournelRepo")
        self.patcher_2 = patch("Service.UserService")
        self.mock_journel_repo = self.patcher.start()
        self.mock_user_service = self.patcher_2.start()
        self.mock_journel_repo.get_all_journel = lambda user_id: self.mocked_get_all_journel(
            user_id)
        self.mock_user_service = MockedUserService()

    def mocked_get_all_journel(self, user_id):
        user_journel = []
        for journel in self.JOURNELS:
            if journel.user_id == user_id:
                user_journel.append(journel)
        return user_journel

        return self.JOURNELS[0]

    def tearDown(self):
        self.patcher.stop()
        self.patcher_2.stop()

    def test_journel_creation(self):
        pass

    def test_get_all_user_journel(self):
        self.journel_manager = JournelManagement(
            self.mock_journel_repo, self.mock_user_service)
        actual = self.journel_manager.get_all_user_journel()
        expected = self.JOURNELS
        self.assertEqual(actual, expected)

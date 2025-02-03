"""Test Script for data repos"""
from unittest import TestCase
from Repository import DataRepo
from unittest.mock import patch, mock_open, Mock
from Data.db import create_connection

DATA = """\
gopal
Hari
Krishna
"""
NO_USER_DATA = """
"""


class MockedConn():
    def __init__(self):
        pass

    def cursor(self):
        mocked_cursor = Mock()
        mocked_cursor.return_value = "Something"
        return mocked_cursor


class TestDataRepo(TestCase):
    """Test case for Data repo"""

    def setUp(self):
        self.test_conn = create_connection(":memory:")
        self.test_cursor = self.test_conn.cursor()
        self.data_repo = DataRepo(self.test_conn)
        self.mock_conn = Mock()
        self.mock_conn.return_value = MockedConn()

    def tearDown(self):
        if self.test_conn:
            if self.test_cursor:
                self.test_cursor.close()
            self.test_conn.close()

    # def test_build_db(self):
    #     self.data_repo.build_db()
    #     self.test_cursor.execute("SELECT * FROM users;")
    #     result = self.test_cursor.fetchall()
    #     self.assertEqual(result[0][0], "Gopal")

    # def setUp(self):
    #     self.data_repo = DataRepo()

    # def test_get_users(self):
    #     m = mock_open(read_data=DATA)
    #     with patch("builtins.open", m):
    #         actual_users = self.data_repo.get_users()
    #     expected_users = ["gopal", "Hari", "Krishna"]
    #     self.assertEqual(actual_users, expected_users)

    # def test_get_users_when_no_users_in_file(self):
    #     m = mock_open(read_data=NO_USER_DATA)
    #     with patch("builtins.open", m):
    #         actual_users = self.data_repo.get_users()
    #     expected_users = []
    #     self.assertEqual(actual_users, expected_users)
    #     # self.assertRaises(FileNotFoundError)

    # def test_get_users_file_not_found(self):
    #     m = mock_open()
    #     with patch("builtins.open", m):
    #         actual_users = self.data_repo.get_users()
    #     self.assertRaises(FileNotFoundError)

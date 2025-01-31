from unittest import TestCase
from Data import create_connection
from Repository import JournelRepo
from sqlite3 import Connection, Error


def make_table(db_conn: Connection):
    cursor = db_conn.cursor()
    try:
        script = ""
        with open("Scripts/db.sql") as scrp:
            script = scrp.read()
        cursor.executescript(script)
    except Error as err:
        print(err)


class TestJournelRepo(TestCase):

    def setUp(self):
        self.test_conn = create_connection(":memory:")
        self.test_cursor = self.test_conn.cursor()
        make_table(self.test_conn)
        query_1 = "INSERT INTO journel(user_id, title, description) VALUES (1, 'TEST JOURNEL', 'TESTING DESCRIPTION')"
        query_2 = "INSERT INTO entry(journel_id, title, content) VALUES (1,'TEST ENTRY1','TEST CONTENT1');"
        self.journel_repo = JournelRepo(self.test_conn)
        try:
            self.test_cursor.execute(query_1)
            self.test_conn.commit()
            self.test_cursor.execute(query_2)
            self.test_conn.commit()
        except Error as err:
            print(err)

    def tearDown(self):
        try:
            if self.test_conn:
                if self.test_cursor:
                    self.test_cursor.close()
                self.test_conn.close()
        except Error as err:
            print(err)

    def test_get_all_journel_for_user(self):
        user_id = 1
        stored_journels = self.journel_repo.get_all_journel(user_id)
        self.assertEqual(stored_journels[0][1], 1)

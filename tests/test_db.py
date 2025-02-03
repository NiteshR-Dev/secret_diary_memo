from unittest import TestCase
import sqlite3

class TestDb(TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        # Creating users table and insert data
        self.cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT, secret_key TEXT)")
        self.cursor.execute("INSERT INTO users (name, password, secret_key) VALUES ('Nitesh Ranjitkar','hero','ABC')")
        self.conn.commit()

    def tearDown(self):
        #Close all DB cursor and connection
        self.cursor.close()
        self.conn.close()

    def test_database_query(self):
        self.cursor.execute("SELECT name, password FROM users ORDER BY name")
        results = self.cursor.fetchall()

        # Define expected results as a list of tuples.
        expected_result = [("Nitesh Ranjitkar", "hero")]
        self.assertEqual(results, expected_result)
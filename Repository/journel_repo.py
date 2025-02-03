from sqlite3 import Connection, Error
from .data_repo import DataRepo
from Data import create_connection


class JournelRepo(DataRepo):

    def __init__(self, db_conn: Connection = create_connection()):
        super().__init__(db_conn)

    def get_all_journel(self, user_id: int):
        cursor = self.db_conn.cursor()
        query = f"SELECT * FROM journel LEFT JOIN entry ON journel.journel_id = entry.journel_id WHERE journel.user_id = {user_id};"
        try:
            result = cursor.execute(query)
            return result.fetchall()
        except Error as err:
            print("Err occured!", err)
            return
        finally:
            cursor.close()
            self.db_conn.close()

    def insert_for_user_1(self):
        cursor = self.db_conn.cursor()
        try:
            # query_1 = "INSERT INTO journel(user_id, title, description) VALUES (2,'2TESTING2','2test description2 is here');"
            # cursor.execute(query_1)
            # self.db_conn.commit()
            # insert_user = "INSERT INTO users(username, password, secret_key) VALUES ('Ram','sitaramjaihanuman','hanumansecretkey');"
            query_2 = "INSERT INTO entry(journel_id, title, content) VALUES (2,'3TEST ENTRY','3TEST CONTENT');"
            cursor.execute(query_2)
            self.db_conn.commit()
            print("SUCCESSFULLY INSERTED DATA")
        except Error as err:
            print("ERRROR OCCURED: ", err)

    def save_new_journel(self, journel_data: dict):
        cursor = self.db_conn.cursor()
        try:
            cursor.execute("INSERT INTO journel(user_id, title, description) VALUES (?,?,?)", journel_data.get(
                "user_id"), journel_data.get("title"), journel_data.get("description"))
            self.db_conn.commit()
        except Error as err:
            print("Error obtained: ", err)

        finally:
            cursor.close()
            self.db_conn.close()

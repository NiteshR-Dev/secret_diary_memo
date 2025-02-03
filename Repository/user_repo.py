"""THIS IS A USER REPOSITORY!!!"""
from Data import Db, create_connection
from sqlite3 import Connection, Error
from Repository import DataRepo
from Data.data import Users


class UserRepository(DataRepo):
    """CRUD User Operations"""

    def __init__(self, db_conn: Connection = create_connection()):
        super().__init__(db_conn)

    def get_users(self) -> list[Users] | list[None]:
        """Get all the users from the db"""

        all_users = []
        users = self.get_all("users")
        for user in users:
            # map users to data class before returning
            all_users.append(Users(*user))
        return all_users

    def save_user(self, user_info_to_save: Users):
        cursor = self.db_conn.cursor()
        try:
            cursor.execute("INSERT INTO users(username, password, secret_key) VALUES (?,?,?)",
                           user_info_to_save.user_name, user_info_to_save.password, user_info_to_save.secret_key)
            self.db_conn.commit()
            saved_data = cursor.execute("SELECT * FROM users WHERE username =? ", user_info_to_save.user_name)
            return saved_data

        except Error as err:
            print("Error has occured: ", err)

        finally:
            cursor.close()
            self.db_conn.close()


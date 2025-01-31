from Data.db import Db
import sqlite3
from sqlite3 import Connection


class DataRepo():
    def __init__(self, db_conn: Connection):
        self.db_conn = db_conn
        # self.db = Db()

    # def __del__(self):
    #     print("Destructor of Repo Called")

    # def get_users(self):
    #     with open("users.txt", "r") as users_file:
    #         lines = users_file.readlines()
    #     users = [line.strip() for line in lines]
    #     if users ==[""]:
    #         return []
    #     return users

    # def get_users_from_db(self):
    #     users = self.db.cursor.execute("SELECT * FROM users ORDER BY name")
    #     res = users.fetchall()
    #     self.db.cursor.close()
    #     self.db.conn.close()
    #     return res

    def __get_script(self, script_file: str = "Scripts/db.sql"):
        sql_script = None
        try:
            with open(script_file) as file:
                sql_script = file.read()
                return sql_script
        except FileNotFoundError as fnf:
            print("Error loading file: ", fnf)

    def build_db(self):
        cur = self.db_conn.cursor()
        try:
            # with open("Scripts/db.sql") as file:
            #     sql_script = file.read()
            #     print(sql_script)
            sql_script = self.__get_script()
            if not sql_script:
                raise FileNotFoundError
            cur.executescript(sql_script)
            # self.db_conn.commit()
            # self.db_conn.close()
        except sqlite3.Error as errors:
            print("Error Occured: ", errors)
        finally:
            self.db_conn.commit()
            cur.close()
            self.db_conn.close()

    def get_all(self, table_name: str):
        """Fetch all data from the table"""
        cursor = self.db_conn.cursor()
        try:
            query = f"SELECT * FROM {table_name};"
            result = cursor.execute(query)
            return result.fetchall()
        except sqlite3.Error as err:
            print(err)
        finally:
            cursor.close()
            self.db_conn.close()
            

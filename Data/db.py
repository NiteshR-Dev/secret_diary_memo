import sqlite3


def create_connection(db_name: str = "Data/example_db.db"):
    conn = None
    try :
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as err:
        print("Error Occured: ", err)
    return conn

class Db():
    """Database"""
    def __init__(self, db="Example.db"):
        self.db = db
        self.conn = self.__connect()
        self.cursor = self.__get_cursor()

    def __del__(self):
        print("Destructor Called!!")
        # self.__disconnect()

    def __connect(self):
        print("Connecting DATABASE!!!!")
        try:
            conn = sqlite3.connect(self.db)
            return conn
        except sqlite3.Error as err:
            print("Errors Found: ", err)

    def __get_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    # def __disconnect(self):
    #     print("DISCONNECTING DATABASE")
    #     self.cursor.close()
    #     self.conn.close()

    def create_user_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (name TEXT, password TEXT, secret_key TEXT)''')
        self.cursor.close()
        self.conn.close()

    def insert_user(self, user_name, password, secret_key):
        self.cursor.execute('''INSERT INTO users VALUES 
                            ('{}','{}', '{}')'''.format(user_name, password, secret_key))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

import pymysql


class DataBase:
    
    __instance = None
    HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "NekitVip123_ZXCPUDGE228"
    DB_NAME = "users"
    
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def get_users(self):
        try:
            connect = pymysql.connect(
                host=self.HOST,
                port=3306,
                user=self.USER,
                password=self.PASSWORD,
                database=self.DB_NAME,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("OK")
            try:
                with connect.cursor() as cursa:
                    get = "SELECT * FROM users.telegram"
                    cursa.execute(get)
                    al = cursa.fetchall()
                    return al
            finally:
                connect.close()
        except Exception as er:
            print("Error")
            print(er)


    def set_table(self, user, idd, city):
        try:
            connect = pymysql.connect(
                host=self.HOST,
                password=self.PASSWORD,
                database=self.DB_NAME,
                port=3306,
                user=self.USER,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("CONNECT SUCCESSFUL")
            try:
                with connect.cursor() as cursa:
                    set_table = f"INSERT INTO `users`.`telegram` (`users`, `id`, `city`) VALUES\
                    ('{user}', '{idd}', '{city}');"
                    cursa.execute(set_table)
                    connect.commit()
            finally:
                connect.close()
        except Exception as er:
            print("Error set")
            print(er)
            return er


    def delete_punct(self, idd, city):
        try:
            connect = pymysql.connect(
                host=self.HOST,
                port=3306,
                database=self.DB_NAME,
                password=self.PASSWORD,
                user=self.USER,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("OK")
            try:
                with connect.cursor() as cursa:
                    delete = f"DELETE FROM `users`.`telegram` WHERE (`id` = '{idd}') and (`city` = '{city}');"
                    cursa.execute(delete)
                    connect.commit()
            finally:
                connect.close()
        except Exception as er:
            print("Error delete")
            print(er)


database = DataBase()
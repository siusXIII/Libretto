import pathlib

import mysql.connector


class DBConnect:

    #@classmethod
    # def getConnection(cls):
    #     try:
    #         cnx = mysql.connector.connect(
    #             user = "root",
    #             password = "password",
    #             host = "127.0.0.1",
    #             database = "libretto")
    #         return cnx
    #     except mysql.connector.Error as err:
    #         print("Non riesco a collegarmi al database")
    #         print(err)
    #         return None

    def __init__(self):
        raise RuntimeError("Non creare una istanza di questa classe!!!")

    _myPool = None

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            try:
                #creo una connessione e restituisco il metodo getConnection()
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(option_files= f"{pathlib.Path(__file__).parent}/connection.cfg",
                                                                          pool_size=3,
                                                                          pool_name="myPool")

                return cls._myPool.get_connection()
            except mysql.connector.Error as err:
                print("Something is wrong in dbConnet")
                print(err)
                return None
        else:
            #se il pool già esiste, restituisco il metodo getConnection()
            return cls._myPool.get_connection()

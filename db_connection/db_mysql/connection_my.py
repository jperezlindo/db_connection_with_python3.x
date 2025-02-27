from mysql.connector import pooling, Error
import sys
class ConnectionMy:

    __DATABASE = ''
    __USERNAME = ''
    __PASSWORD = ''
    __DB_PORT = ''
    __HOST = ''
    __POOL_SIZE = 5
    __POOL_NAME = ''
    __pool = None

    # Allows to get a connections pool
    @classmethod
    def get_pool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pooling.MySQLConnectionPool(
                    pool_name=cls.__POOL_NAME,
                    pool_size=cls.__POOL_SIZE,
                    database=cls.__DATABASE,
                    username=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    host=cls.__HOST
                )
                return cls.__pool
            except Exception as e:
                #you can driver exceptions however you want!
                print(e)
                sys.exit()
        else:
            return cls.__pool

#    Allows to get a connection from connections pool
    @classmethod
    def get_conn(cls):
        pool = cls.get_pool()
        if pool is not None:
            return pool.get_connection()

    # Releases and returns a connection to connections pool
    @classmethod
    def release_connection(cls, conn):
        conn.close()
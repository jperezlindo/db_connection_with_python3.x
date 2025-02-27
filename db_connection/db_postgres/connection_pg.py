from psycopg2 import pool
import sys

class ConnectionPG:

    __MIN_CONN = 1
    __MAX_CONN = 5
    __USER = ''
    __PASSWORD = ''
    __HOST = ''
    __DB_PORT = ''
    __DATABASE = ''
    __pool = None

    # Allows to get a connections pool
    @classmethod
    def get_pool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CONN,
                    cls.__MAX_CONN,
                    user = cls.__USER,
                    password = cls.__PASSWORD,
                    host = cls.__HOST,
                    port = cls.__DB_PORT,
                    database = cls.__DATABASE
                )
                return cls.__pool
            except Exception as e:
                #you can driver exceptions however you want!
                print(e)
                sys.exit()
        else:
            return cls.__pool

    # Allows to get a connection from connections pool
    @classmethod
    def get_connection(cls):
        try:
            conn = cls.get_pool().getconn()
            return conn
        except Exception as e:
            #you can driver exceptions however you want!
            print(e)
            sys.exit()

    # Releases and returns a connection to connections pool
    @classmethod
    def release_connection(cls, conn):
        cls.get_pool().putconn(conn)

    # Closes connections pool
    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()
from connection_pg import ConnectionPG

class PoolCursorPG():

    def __init__(self) -> None:
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = ConnectionPG.get_connection()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn is not None:
            if exc_val:
                self._conn.rollback()
                #you can driver exceptions however you want!
                print(exc_type, exc_val, exc_tb)
            else:
                self._conn.commit()

            if self._cursor is not None:
                self._cursor.close()

            ConnectionPG.release_connection(self._conn)
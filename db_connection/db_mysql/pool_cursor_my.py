from connection_my import ConnectionMy

class PoolCursorMy():

    def __init__(self) -> None:
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = ConnectionMy.get_conn()
        if self._conn is not None:
            self._cursor = self._conn.cursor()
            return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn is not None:
            if exc_val:
                #you can driver exceptions however you want!
                self._conn.rollback()
            else:
                self._conn.commit()

        if self._cursor is not None:
            self._cursor.close()

        ConnectionMy.release_connection(self._conn)
import pyodbc
from util.property_util import PropertyUtil
from exception.database_exception import DatabaseConnectionException


class DBConnection:
    def __init__(self):
        try:
            conn_str = PropertyUtil.fetch_connection_string()
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except Exception as error:
            raise DatabaseConnectionException("Connection failed!") from error

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

# coding: utf-8


class BaseConnector:
    """
    The base class for all connectors.
    Mainly declare the attributes and methods,
    provides some helpful methods in addition.
    """

    def __init__(self):
        self._db = ""
        self._conn = None
        self.cursor = None
        self.attribute = None
        self.target = ""
        self.target_info = ""

    def connect(self, **kwargs):
        """
        Establish the connection to the target database.
        return the connection object of the target.
        Limited attributes provided to be costumed.
        It's a simple frame anyway.
        """
        pass

    @property
    def transaction(self):
        """
        Return the current state of the transaction.(True or False)
        """
        return None

    @property
    def database(self):
        """
        Return name of the using database
        """
        return self._db

    def select_db(self, database):
        """
        Change the database, however some databases like sqlite may cannot change database.
        The implement may be weird.
        """
        pass

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def disconnect(self):
        self.cursor.close()
        self._conn.close()
        self.cursor = None
        self._conn = None


class ConnectionException(BaseException):
    pass


from .sqlite_connector import SQLiteConnector
from .mysql_connector import MysqlConnector

# When some more connector added, be sure
# the name(PROTO in URL) and the Class in
# this dict to use them normally
connector_map = {
    "sqlite": SQLiteConnector,
    "mysql": MysqlConnector
}

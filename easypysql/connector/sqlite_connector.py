# coding: utf-8

import sqlite3
from .base import *


class SQLiteConnector(BaseConnector):
    def __init__(self, database=None, timeout=None, isolation_level=None, uri=None, **kwargs):
        super(SQLiteConnector, self).__init__()
        self._db = database
        self.target = "SQLite"
        self.target_info = "SQLite %s" % sqlite3.sqlite_version
        self.attribute = {
            "database": database,
            "timeout": timeout,
            "isolation_level": isolation_level,
            "uri": uri
        }
        self._conn = self.connect(**self.attribute)

    def connect(self, **kwargs):
        """
        Establish the connection to the sqlite3 database.
        """
        try:
            if kwargs['database'] is None:
                raise ConnectionException("Database cannot be None.")
            self._conn = sqlite3.connect(kwargs['database'])
        except sqlite3.Error as e:
            raise ConnectionException(e)
        if self._conn:
            self.cursor = self._conn.cursor()

    @property
    def transaction(self):
        return self._conn.in_transaction

    @property
    def database(self):
        return self._db

    def select_db(self, db):
        """
        Although sqlite3 regards a database as a file,
        we still implement database change as reconnect to the new file
        """
        if self._conn:
            self._conn.close()
        self._conn = self.connect(**self.attribute)

    def execute(self, sql):
        self.cursor.execute(sql)

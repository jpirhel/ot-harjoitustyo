import logging
import sqlite3

from ..stop import Stop
# from ..trip import Trip
# from ..route import Route

from ...constant import SQLITE_FILE_NAME


class Reader:
    """Class for reading data from SQLite database"""

    def __init__(self):
        self._log = logging.getLogger("Reader")

        try:
            self._sqlite = sqlite3.connect(SQLITE_FILE_NAME)
        except sqlite3.Error:
            self._log.error(
                "Failed to connect to sqlite database: %s", SQLITE_FILE_NAME)

        self._log.info("Reader initialized")

    def read_stops(self):
        """Reads data for all stops_data from SQLite"""

        sql = """
            SELECT * from stop
        """

        res = self._execute_sql(sql)

        stops_data = res.fetchall()

        stops = []

        for stop_data in stops_data:
            stop = Stop.from_database(stop_data)
            stops.append(stop)

        return stops

    def read_stop(self, stop_id=None):
        """Reads single stop data from SQLite"""

        if stop_id is None:
            self._log.error("Can't read stop, stop_id: %s", stop_id)
            return

    def _execute_sql(self, sql):
        """Executes a single SQL statement in SQLite database"""

        self._log.info("Executing sql: %s", sql)

        try:
            cursor = self._sqlite.cursor()
            res = cursor.execute(sql)
        except sqlite3.Error as error:
            self._log.error("Failed to execute SQL: %s, error: %s", sql, error)
            return None

        return res

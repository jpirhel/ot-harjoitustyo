import logging
import sqlite3

from ..stop import Stop
# from ..trip import Trip
# from ..route import Route

from ...constant import SQLITE_FILE_NAME


class Reader:
    """Reads data from SQLite database."""

    def __init__(self, file_name=SQLITE_FILE_NAME):
        """Initializes an instance of the Reader class.

        Args:
             file_name: Name of the SQLite database file
        """

        self._log = logging.getLogger("Reader")

        try:
            self._sqlite = sqlite3.connect(file_name)
            self._log.info("Reader initialized")
        except sqlite3.Error:
            self._log.error(
                "Failed to connect to sqlite database: %s", file_name)

    def read_stops(self):
        """Reads data for all stops_data from SQLite.

        Returns: a list of instances of the class Stop
        """

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
        """Reads single stop data from SQLite.

        Args:
            stop_id: id for the Stop

        Returns: an instance of the Stop class or None

        """

        if stop_id is None:
            self._log.error("Can't read stop, stop_id: %s", stop_id)
            return

        sql = """
            SELECT * from stop where id=?
        """

        res = self._execute_sql(sql, (stop_id,))
        data = res.fetchone()

        stop = Stop.from_database(data)

        return stop

    def _execute_sql(self, sql, sql_args=None):
        """Executes a single SQL statement in the SQLite database.

        Args:
            sql: SQL statement to be executed
            sql_args: Tuple of SQL arguments
        """

        self._log.info("Executing sql: %s", sql)

        try:
            cursor = self._sqlite.cursor()

            if sql_args is not None:
                res = cursor.execute(sql, sql_args)
            else:
                res = cursor.execute(sql)
        except sqlite3.Error as error:
            self._log.error("Failed to execute SQL: %s, error: %s", sql, error)
            return None

        return res

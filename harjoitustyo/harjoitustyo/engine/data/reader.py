import logging
import sqlite3

from ..stop import Stop
from ..stop_time import StopTime

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
        """Reads data for all stops from SQLite.

        Returns:
             a list of instances of the class Stop
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

        Returns:
            an instance of the Stop class or None
        """

        if stop_id is None:
            self._log.error("Can't read stop, stop_id: %s", stop_id)
            return None

        sql = """
            SELECT * from stop where id=?
        """

        res = self._execute_sql(sql, (stop_id,))
        data = res.fetchone()

        stop = Stop.from_database(data)

        return stop

    def read_stop_times(self, stop=None):
        """Reads stop timetable data for a single stop from SQLite.

        Args:
            stop: a single Stop

        Returns:
            a list of instances of the class StopTime
        """

        if stop is None:
            self._log.error("Can't read stop times, stop: %s", stop)
            return None

        sql = """

        SELECT
            stop_time.trip_id,
            stop_time.arrival_time,
            stop_time.departure_time,
            stop_time.stop_id,
            stop_time.stop_sequence,
            stop_time.stop_headsign,
            stop_time.pickup_type,
            stop_time.drop_off_type,
            stop_time.shape_dist_traveled,
            stop_time.timepoint,
            route.route_short_name

        FROM stop_time

        JOIN trip
        ON stop_time.trip_id = trip.trip_id

        JOIN route
        ON trip.route_id = route.route_id

        WHERE stop_id = (SELECT id FROM stop WHERE stop_code = ?)

        ORDER BY stop_time.arrival_time
        """

        res = self._execute_sql(sql, (stop.stop_code,))

        data = res.fetchall()

        stop_times = []

        for datum in data:
            stop_time = StopTime.from_database_with_route_short_name(datum)
            stop_times.append(stop_time)

        return stop_times

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

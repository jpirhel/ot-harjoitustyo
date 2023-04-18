import os
import logging
import pathlib
import tempfile
import zipfile
import sqlite3

from ..stop import Stop
from ..route import Route
from ..trip import Trip


class ZipImporter:
    _sqlite_file_name = "database.sqlite"

    def __init__(self, data_file=None):
        if data_file is None:
            raise AttributeError("Can't import empty file!")

        self._data_file = data_file

        self._initialize_sqlite()

        self._tmp_dir = None

        self._log = logging.getLogger("DataImporter")

    def import_data(self):
        """Imports data from zipped HSL file"""

        self._unzip_data_file()
        self._import_data_directory()

    def _unzip_data_file(self):
        """Unzips HSL data file into a temporary directory"""

        try:
            path = pathlib.Path(self._data_file.name)
        except AttributeError:
            #  support string only path for local testing
            path = pathlib.Path(self._data_file)

        self._log.info("Data file path: %s", path)

        if not path.is_file():
            raise FileNotFoundError("Zip file doesn't exist")

        # pylint: disable=consider-using-with
        # reasoning: temporary directory should not be cleaned up yet

        tmp_dir = tempfile.TemporaryDirectory()

        # pylint: enable=consider-using-with

        with zipfile.ZipFile(path, "r") as zip_file:
            zip_file.extractall(tmp_dir.name)

        self._tmp_dir = tmp_dir

    def _import_data_directory(self):
        stops_1 = "stops.txt"  # names of public transport stops
        stops_2 = "stops2.txt"  # some versions of the Zip file have a stops2.txt file
        stop_times = "stop_times.txt"  # timetables for the stops
        trips = "trips.txt"
        routes = "routes.txt"

        # files = [trips, routes, stops_1, stops_2, stop_times]
        # files = [trips, routes, stops_1, stops_2]
        files = [trips, routes]

        for file in files:
            self._import_file(file)

    def _import_file(self, file_name=None):
        """Imports a single data file to SQLite"""

        if not file_name:
            raise FileNotFoundError("Can't find empty file!")

        path = pathlib.Path(self._tmp_dir.name, file_name)

        if not path.is_file():
            self._log.error("Can't find file!")
            return

        with open(path.absolute(), "r", encoding="UTF-8") as data_file:
            lines = data_file.readlines()

            for line in lines:
                self._insert_datum(file_name, line)

    def _initialize_sqlite(self):
        """Initializes SQLite file for data storage"""

        # delete old SQLite file

        path = pathlib.Path(self._sqlite_file_name)

        if path.is_file():
            os.remove(path.absolute())

        self._sqlite = sqlite3.connect(self._sqlite_file_name)

        cursor = self._sqlite.cursor()

        create_table_stop = """
            CREATE TABLE stop (
                id integer PRIMARY KEY,
                stop_code text,
                stop_name text,
                stop_desc text,
                stop_lat text,
                stop_lon text,
                zone_id text,
                stop_url text,
                location_type integer,
                parent_station integer,
                wheelchair_boarding integer,
                platform_code text,
                vehicle_type integer
            );
        """

        cursor.execute(create_table_stop)

        create_table_trip = """
            CREATE TABLE trip (
                route_id str,
                service_id str,
                trip_id str PRIMARY KEY,
                trip_headsign str,
                direction_id str,
                shape_id str,
                wheelchair_accessible str,
                bikes_allowed str,
                max_delay str
            );
        """

        cursor.execute(create_table_trip)

    def _insert_datum(self, file_name, line):
        """Inserts a single datum to SQLite, based on the type"""

        if file_name == "stops.txt":
            self._insert_stop(line)

        if file_name == "stops2.txt":
            self._insert_stop(line)

        if file_name == "stop_times.txt":
            self._insert_stop_time(line)

        if file_name == "trips.txt":
            self._insert_trip(line)

        if file_name == "routes.txt":
            self._insert_route(line)

    def _insert_stop(self, line):
        """Inserts a datum for single public transport stop"""

        print(f"STOP: {line.rstrip()}")

        stop = Stop.from_string(line)

        if stop is None:
            self._log.error("Couldn't insert stop: %s, line: %s", stop, line)
            return

        # NOTE: this is probably inefficient

        cursor = self._sqlite.cursor()

        # pylint: disable=duplicate-code
        # reasoning: this duplication is SQL vs. normal python code in class Stop

        sql = """
            INSERT INTO stop(
                id,
                stop_code,
                stop_name,
                stop_desc,
                stop_lat,
                stop_lon,
                zone_id,
                stop_url,
                location_type,
                parent_station,
                wheelchair_boarding,
                platform_code,
                vehicle_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # pylint: enable=duplicate-code

        cursor.execute(sql, stop.as_list())
        self._sqlite.commit()
        cursor.close()

    def _insert_stop_time(self, line):
        """Inserts a datum for single public transport stop timetable"""

        print(f"_insert_stop_time: {line}")

    def _insert_route(self, line):
        """Inserts a datum for single public transport route"""

        print(f"ROUTE: {line.rstrip()}")

        route = Route.from_string(line)

        if route is None:
            self._log.error("Couldn't insert route: %s, line: %s", route, line)
            return

        cursor = self._sqlite.cursor()

        # pylint: disable=duplicate-code
        # reasoning: this duplication is SQL vs. normal python code in class Stop

        sql = """
            INSERT INTO route(
                route_id,
                agency_id,
                route_short_name,
                route_long_name,
                route_desc,
                route_type,
                route_url
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        # pylint: enable=duplicate-code

        cursor.execute(sql, route.as_list())
        self._sqlite.commit()
        cursor.close()
    def _insert_trip(self, line):
        """Inserts a datum for single public transport trip"""

        print(f"TRIP: {line.rstrip()}")

        trip = Trip.from_string(line)

        if trip is None:
            self._log.error("Couldn't insert trip: %s, line: %s", trip, line)
            return

        cursor = self._sqlite.cursor()

        # pylint: disable=duplicate-code
        # reasoning: this duplication is SQL vs. normal python code in class Stop

        sql = """
            INSERT INTO trip(
                route_id,
                service_id,
                trip_id,
                trip_headsign,
                direction_id,
                shape_id,
                wheelchair_accessible,
                bikes_allowed,
                max_delay
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # pylint: enable=duplicate-code

        cursor.execute(sql, trip.as_list())
        self._sqlite.commit()
        cursor.close()

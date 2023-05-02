import sqlite3
import unittest

from harjoitustyo.constant import SQLITE_FILE_NAME
from harjoitustyo.engine.data.reader import Reader
from harjoitustyo.engine.stop import Stop


class TestReader(unittest.TestCase):
    def setUp(self) -> None:
        self.reader = Reader(file_name=SQLITE_FILE_NAME)

    def test_reader_initialized_correctly(self):
        self.assertIsInstance(self.reader, Reader)

    def test_read_stops(self):
        stops = self.reader.read_stops()

        self.assertIsInstance(stops, list)

    def test_read_stop_id_empty(self):
        stop_id = None
        stop = self.reader.read_stop(stop_id)

        self.assertIsNone(stop)

    def test_read_stop(self):
        stop_id = "1230109"
        stop = self.reader.read_stop(stop_id)

        self.assertIsInstance(stop, Stop)

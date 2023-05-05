import unittest

from harjoitustyo.constant import SQLITE_FILE_NAME
from harjoitustyo.engine.data.reader import Reader
from harjoitustyo.engine.stop import Stop


class TestReader(unittest.TestCase):
    def setUp(self) -> None:
        self.reader = Reader(file_name=SQLITE_FILE_NAME)

        stop_data = """1230109,H3037,"Kumpulan kampus","Hämeentie",60.203120,24.967300,A,http://aikataulut.hsl.fi/pysakit/fi/1230109.html,0, ,2, ,3"""
        self.stop = Stop.from_string(stop_data)

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

    def test_read_stops_empty_stop(self):
        res = self.reader.read_stop_times(None)

        self.assertIsNone(res)

    def test_read_stop_times(self):
        res = self.reader.read_stop_times(self.stop)

        self.assertIsNotNone(res)

        # minimum number of elements fetched from database
        list_min_length = 10

        list_has_elements = len(res) > list_min_length

        self.assertTrue(list_has_elements)

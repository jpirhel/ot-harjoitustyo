import unittest

from harjoitustyo.engine.stop import Stop
from harjoitustyo.engine.marker import Marker


class TestMarker(unittest.TestCase):
    """Tests the functionality of the Marker data class."""

    def setUp(self):
        """Initializes Stop instance from provided data and uses the data to create a Marker instance."""

        stop_data = """1230109,H3037,"Kumpulan kampus","Hämeentie",60.203120,24.967300,A,http://aikataulut.hsl.fi/pysakit/fi/1230109.html,0, ,2, ,3"""
        stop = Stop.from_string(stop_data)

        self.marker = Marker(stop.stop_name, stop.stop_lat, stop.stop_lon)

    def test_marker_creation(self):
        self.assertIsInstance(self.marker, Marker)

    def test_marker_name_correct(self):
        self.assertEqual(self.marker.name, "Kumpulan kampus")

    def test_marker_lat_correct(self):
        self.assertEqual(self.marker.lat, 60.203120)

    def test_marker_lon_correct(self):
        self.assertEqual(self.marker.lon, 24.967300)

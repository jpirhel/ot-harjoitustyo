import unittest

from harjoitustyo.engine.stop import Stop


class TestStop(unittest.TestCase):
    """Test the functionality of the Stop data class"""

    def setUp(self):
        """Initialize an instance of the Stop data class from provided data"""

        stop_data = """1230109,H3037,"Kumpulan kampus","Hämeentie",60.203120,24.967300,A,http://aikataulut.hsl.fi/pysakit/fi/1230109.html,0, ,2, ,3"""
        self.stop = Stop.from_string(stop_data)

    def test_stop_creation(self):
        self.assertIsInstance(self.stop, Stop)

    def test_stop_code_correct(self):
        self.assertEqual(self.stop.stop_code, "H3037")

    def test_stop_name_correct(self):
        self.assertEqual(self.stop.stop_name, "Kumpulan kampus")

    def test_stop_lat_correct(self):
        self.assertEqual(self.stop.stop_lat, 60.203120)

    def test_stop_lon_correct(self):
        self.assertEqual(self.stop.stop_lon, 24.967300)

import unittest

from harjoitustyo.engine.stop import Stop


class TestStop(unittest.TestCase):
    """Tests the functionality of the Stop data class."""

    def setUp(self):
        """Initializes the required Stop instances."""

        # instance from string data

        stop_data = """1230109,H3037,"Kumpulan kampus","Hämeentie",60.203120,24.967300,A,http://aikataulut.hsl.fi/pysakit/fi/1230109.html,0, ,2, ,3"""
        self.stop = Stop.from_string(stop_data)

        # instance from header data

        header_data = """stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,wheelchair_boarding,platform_code,vehicle_type"""
        self.header = Stop.from_string(header_data)

        # instance from string data with an element containing a comma (length 14)

        len14_data = """1040289,H1260,"Kamppi, tulo","Kamppi",60.168800,24.930120,A,http://aikataulut.hsl.fi/pysakit/fi/1040289.html,0,1000001,0, ,3"""
        self.len14_stop = Stop.from_string(len14_data)

    def test_header_creation(self):
        self.assertIsNone(self.header)

    def test_len14_creation(self):
        self.assertIsInstance(self.len14_stop, Stop)

    def test_len14_name(self):
        self.assertEqual(self.len14_stop.stop_name, "Kamppi, tulo")

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

    def test_stop_getter_lat_type(self):
        self.assertIsInstance(self.stop.lat, float)

    def test_stop_getter_lon_type(self):
        self.assertIsInstance(self.stop.lon, float)

    def test_stop_getter_coord(self):
        coord = self.stop.coord()
        self.assertIsInstance(coord, tuple)

        lat = coord[0]
        lon = coord[1]

        self.assertIsInstance(lat, float)
        self.assertIsInstance(lon, float)

    def test_stop_creation_from_database_data(self):
        data = [
            "1010107",
            "H2014",
            "Meritullinkatu",
            "Liisankatu",
            "60.174128",
            "24.955551",
            "A",
            "http://aikataulut.hsl.fi/pysakit/fi/1010107.html",
            "0",
            "",
            "2",
            "",
            "3"
        ]

        stop = Stop.from_database(data)

        self.assertIsInstance(stop, Stop)

    def test_corrected_stop_url(self):
        correct_url = "https://reittiopas.hsl.fi/pysakit/HSL%3A1230109"

        stop_url = self.stop.corrected_stop_url()

        self.assertEqual(correct_url, stop_url)

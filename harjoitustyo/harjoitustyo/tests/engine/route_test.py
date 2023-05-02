import unittest

from harjoitustyo.engine.route import Route


class TestRoute(unittest.TestCase):
    """Tests the functionality of the Route data class."""

    def setUp(self):
        """Initializes Route data class from provided data and use the data to create the Route data class instance."""

        route_data = """1001,HSL,1,Eira - Töölö - Sörnäinen (M) - Vallila,,0,http://aikataulut.hsl.fi/linjat/fi/h1_1a.html"""
        route = Route.from_string(route_data)
        self.route = route

        header_data = """route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url"""
        header = Route.from_string(header_data)
        self.header = header

    def test_header_creation(self):
        self.assertIsNone(self.header)

    def test_route_creation(self):
        self.assertIsInstance(self.route, Route)

    def test_route_id_correct(self):
        self.assertEqual(self.route.route_id, "1001")

    def test_route_short_name_correct(self):
        self.assertEqual(self.route.route_short_name, "1")

    def test_route_long_name_correct(self):
        self.assertEqual(self.route.route_long_name,
                         "Eira - Töölö - Sörnäinen (M) - Vallila")

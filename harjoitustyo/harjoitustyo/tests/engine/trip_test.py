import unittest

from harjoitustyo.engine.trip import Trip


class TestTrip(unittest.TestCase):
    """Test the functionality of the Trip data class"""

    def setUp(self):
        """Initialize Trip data class from provided data and use the data to create the Trip data class instance"""

        trip_data = """1001,1001_20230417_20230531_Ke,1001_20230417_Ke_1_0540,"Vallila",0,1001_20230306_1,1,2,3"""
        trip = Trip.from_string(trip_data)

        self.trip = trip

    def test_route_creation(self):
        self.assertIsInstance(self.trip, Trip)

    def test_trip_route_id_correct(self):
        self.assertEqual(self.trip.route_id, "1001")

    def test_trip_trip_id_correct(self):
        self.assertEqual(self.trip.trip_id, "1001_20230417_Ke_1_0540")

    def test_trip_headsign_correct(self):
        self.assertEqual(self.trip.trip_headsign, "Vallila")
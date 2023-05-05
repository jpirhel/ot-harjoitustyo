import unittest

from harjoitustyo.engine.stop_time import StopTime


class TestStopTime(unittest.TestCase):
    """Tests the functionality of the StopTime class."""

    def setUp(self) -> None:
        """Initializes the required instances of the StopTime class."""

        stop_time_data = """1001_20230417_Ke_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        stop_time_data_with_route_short_name = """1001_20230417_Ke_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1,1"""
        header_data = """trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint"""

        # instance from string data

        self.stop_time = StopTime.from_string(stop_time_data)

        # instance from header string data

        self.header = StopTime.from_string(header_data)

        # instance from database (list) data

        database_data = stop_time_data.split(",")
        self.stop_time_from_database = StopTime.from_database(database_data)

        # instance from database data with route short name

        database_data_with_route_short_name = stop_time_data_with_route_short_name.split(",")
        self.with_short_route_name = StopTime.from_database_with_route_short_name(
            database_data_with_route_short_name)

    def test_header_creation(self):
        self.assertIsNone(self.header)

    def test_stop_time_creation(self):
        self.assertIsInstance(self.stop_time, StopTime)

    def test_from_database_data(self):
        self.assertIsInstance(self.stop_time_from_database, StopTime)

    def test_from_database_data_with_route_short_name(self):
        self.assertIsInstance(self.with_short_route_name, StopTime)

    def test_repr_without_route_short_name(self):
        correct = "1050417"
        self.assertEqual(str(self.stop_time), correct)

    def test_repr_with_route_short_name(self):
        correct = "('1050417', '1')"
        self.assertEqual(str(self.with_short_route_name), correct)

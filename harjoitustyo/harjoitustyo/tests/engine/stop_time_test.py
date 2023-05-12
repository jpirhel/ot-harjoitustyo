import unittest

from harjoitustyo.constant import ERROR_WEEKDAY, ERROR_TIME
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

        # synthetic data to test weekdays

        data_wed = """1001_20230417_Ke_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        self.stop_time_wed = StopTime.from_string(data_wed)

        data_sat = """1001_20230417_La_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        self.stop_time_sat = StopTime.from_string(data_sat)

        data_sun = """1001_20230417_Su_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        self.stop_time_sun = StopTime.from_string(data_sun)

        data_erroneous_trip_id = """1001_20230417_Su_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        self.stop_time_erroneous_trip_id = StopTime.from_string(data_erroneous_trip_id)
        self.stop_time_erroneous_trip_id.trip_id = "NOT_WORKING"

        data_erroneous_weekday = """1001_20230417_XX_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        self.stop_time_erroneous_weekday = StopTime.from_string(data_erroneous_weekday)

    def test_header_creation(self):
        self.assertIsNone(self.header)

    def test_stop_time_creation(self):
        self.assertIsInstance(self.stop_time, StopTime)

    def test_from_database_data(self):
        self.assertIsInstance(self.stop_time_from_database, StopTime)

    def test_from_database_data_with_route_short_name(self):
        self.assertIsInstance(self.with_short_route_name, StopTime)

    def test_stop_time_weekdays(self):
        self.assertEqual(self.stop_time_wed.weekday(), 0)
        self.assertEqual(self.stop_time_sat.weekday(), 5)
        self.assertEqual(self.stop_time_sun.weekday(), 6)

    def test_stop_time_hour(self):
        self.assertEqual(self.stop_time.hour(), 5)

    def test_stop_time_minute(self):
        self.assertEqual(self.stop_time.minute(), 40)

    def test_stop_time_display_time(self):
        self.assertEqual(self.stop_time.display_time(), "05:40")

    def test_stop_time_erroneous_trip_id(self):
        self.assertEqual(self.stop_time_erroneous_trip_id.weekday(), ERROR_WEEKDAY)
        self.assertEqual(self.stop_time_erroneous_trip_id.hour(), ERROR_TIME)
        self.assertEqual(self.stop_time_erroneous_trip_id.minute(), ERROR_TIME)

    def test_stop_time_erroneous_weekday(self):
        self.assertEqual(self.stop_time_erroneous_weekday.weekday(), ERROR_WEEKDAY)

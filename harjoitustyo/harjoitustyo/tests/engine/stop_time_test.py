import unittest

from harjoitustyo.engine.stop_time import StopTime


class TestStopTime(unittest.TestCase):
    """Tests the functionality of the StopTime class."""

    def setUp(self) -> None:
        """Initializes an instance of StopTime class."""

        stop_time_data = """1001_20230417_Ke_1_0540,05:40:00,05:40:00,1050417,1,"Vallila via Lasipalatsi",0,1,0.000,1"""
        header_data = """trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint"""

        self.stop_time = StopTime.from_string(stop_time_data)
        self.header = StopTime.from_string(header_data)

    def test_header_creation(self):
        self.assertIsNone(self.header)

    def test_stop_time_creation(self):
        self.assertIsInstance(self.stop_time, StopTime)

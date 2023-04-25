import unittest

from harjoitustyo.constant import KUMPULA_LAT, KUMPULA_LON, ZOOM_DEFAULT, ZOOM_MAX, ZOOM_MIN, \
    MAXIMUM_STOP_DISTANCE_FROM_CENTER, SQLITE_FILE_NAME, BUTTON_DEFAULT_WIDTH, BUTTON_DEFAULT_HEIGHT


class TestConstant(unittest.TestCase):
    def setUp(self) -> None:
        self._KUMPULA_LAT = KUMPULA_LAT
        self._KUMPULA_LON = KUMPULA_LON
        self._ZOOM_DEFAULT = ZOOM_DEFAULT
        self._ZOOM_MAX = ZOOM_MAX
        self._ZOOM_MIN = ZOOM_MIN
        self._MAXIMUM_STOP_DISTANCE_FROM_CENTER = MAXIMUM_STOP_DISTANCE_FROM_CENTER
        self._SQLITE_FILE_NAME = SQLITE_FILE_NAME
        self._BUTTON_DEFAULT_WIDTH = BUTTON_DEFAULT_WIDTH
        self._BUTTON_DEFAULT_HEIGHT = BUTTON_DEFAULT_HEIGHT

    def test_kumpula_lat_correct_type(self):
        self.assertIsInstance(self._KUMPULA_LAT, float)

    def test_kumpula_lon_correct_type(self):
        self.assertIsInstance(self._KUMPULA_LON, float)

    def test_zoom_default_correct_type(self):
        self.assertIsInstance(self._ZOOM_DEFAULT, int)

    def test_zoom_max_correct_type(self):
        self.assertIsInstance(self._ZOOM_MAX, int)

    def test_zoom_min_correct_type(self):
        self.assertIsInstance(self._ZOOM_MIN, int)

    def test_maximum_stop_distance_from_center_correct_type(self):
        self.assertIsInstance(self._MAXIMUM_STOP_DISTANCE_FROM_CENTER, float)

    def test_sqlite_file_name_correct_type(self):
        self.assertIsInstance(self._SQLITE_FILE_NAME, str)

    def test_button_default_width_correct_type(self):
        self.assertIsInstance(self._BUTTON_DEFAULT_WIDTH, int)

    def test_button_default_height_correct_type(self):
        self.assertIsInstance(self._BUTTON_DEFAULT_HEIGHT, int)

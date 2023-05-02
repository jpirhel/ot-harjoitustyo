import pathlib
import unittest

from harjoitustyo.constant import DATA_URL, DATA_FILE_NAME
from harjoitustyo.engine.data.fetcher import Fetcher


class TestFetcher(unittest.TestCase):
    """Tests the functionality of the Tester class."""

    # noinspection PyMethodMayBeStatic
    def _zip_path(self, file_name):
        return file_name

    def setUp(self):
        data_url = DATA_URL

        self.fetcher = Fetcher(data_url=data_url)

    def test_no_data_url(self):
        with self.assertRaises(AttributeError):
            _ = Fetcher(data_url=None)

    def test_fetching_not_skipped(self):
        #  Note: Testing fetching depends on HSL.fi website working

        self.fetcher.fetch()

        path = pathlib.Path(self._zip_path(DATA_FILE_NAME))
        print(path)

        self.assertTrue(path.is_file())

    def test_fetching_skipped(self):
        # NOTE: should be run after the non-skipped version which downloads the zip file

        self.fetcher.fetch(skip_fetching=True)

        path = pathlib.Path(self._zip_path(DATA_FILE_NAME))

        self.assertTrue(path.is_file())

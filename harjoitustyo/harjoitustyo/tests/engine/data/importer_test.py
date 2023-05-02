import unittest

from harjoitustyo.engine.data.importer import Importer


class TestImporter(unittest.TestCase):
    """Tests the functionality of the Importer class.

    Note: Actually importing the data would slow down testing significantly,
    therefore skip_importing is set to True.
    """

    def setUp(self) -> None:
        self.importer = Importer()

    def test_import_data_skipped(self):
        success = self.importer.import_data(skip_fetching=False, skip_importing=True)

        self.assertTrue(success)

    def test_import_data_not_skipped(self):
        success = self.importer.import_data(skip_fetching=True, skip_importing=True)

        self.assertTrue(success)

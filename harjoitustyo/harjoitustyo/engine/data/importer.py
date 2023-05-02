import logging


from .fetcher import Fetcher
from .zip_importer import ZipImporter
from ...constant import SKIP_FETCHING


class Importer:
    """Imports data from web to SQLite database.

    The data resides on HSL servers and is periodically refreshed. Realtime information
    is not used, because that requires an API key.
    """

    def __init__(self):
        self._log = logging.getLogger("Importer")

    def import_data(self, skip_fetching=SKIP_FETCHING, skip_importing=False):
        """Fetches and imports data into SQLite file.

        Args:
            skip_fetching: Skip actual fetching of data from the Web
            skip_importing: Skip actual importing of data into SQLite database

        Returns: True on success
        """

        self._log.info("Importing data...")

        fetcher = Fetcher()
        fetcher.fetch(skip_fetching=skip_fetching)

        zip_filename = fetcher.data_file

        self._log.info("Zip file: %s", zip_filename)

        if skip_importing is False:
            # Actually import the data from the zip file to the SQLite database.
            # NOTE: This might take a long time (tens of minutes).

            zip_importer = ZipImporter(data_file=zip_filename)
            zip_importer.import_data()

        self._log.info("...Done.")

        return True

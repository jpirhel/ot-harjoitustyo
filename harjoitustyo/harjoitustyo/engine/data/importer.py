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

    def import_data(self):
        """Fetches and imports data into SQLite file."""

        self._log.info("Importing data...")

        # set to True to skip fetching when testing locally
        skip_fetching = SKIP_FETCHING

        fetcher = Fetcher()
        fetcher.fetch(skip_fetching=skip_fetching)

        zip_filename = fetcher.data_file

        self._log.info("Zip file: %s", zip_filename)

        zip_importer = ZipImporter(data_file=zip_filename)
        zip_importer.import_data()

        self._log.info("...Done.")

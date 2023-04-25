import logging


from .fetcher import Fetcher
from .zip_importer import ZipImporter


class Importer:
    """Imports data from web to SQLite database

    The data resides on HSL servers and is periodically refreshed. Realtime information is not used,
    because that requires an API key.
    """

    def __init__(self):
        self._log = logging.getLogger("Importer")

    def import_data(self):
        """Fetches and imports data into SQLite file"""
        self._log.info("Importing data...")

        # set to True to skip fetching when testing locally
        skip_fetching = True

        fetcher = Fetcher()
        fetcher.fetch(skip_fetching=skip_fetching)

        # zip_filename = fetcher.data_file
        # zip_filename = "c:\\Users\jpir\IdeaProjects\opiskelu\ot-harjoitustyo\harjoitustyo\HSL.zip"
        zip_filename = "HSL.zip"
        self._log.info("Zip file: %s", zip_filename)

        zip_importer = ZipImporter(data_file=zip_filename)
        zip_importer.import_data()

        self._log.info("...Done.")

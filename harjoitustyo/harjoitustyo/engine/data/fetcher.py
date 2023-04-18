import os
import logging
import requests


# Data URL from https://www.hsl.fi/hsl/avoin-data
DATA_URL = "https://infopalvelut.storage.hsldev.com/gtfs/hsl.zip"


class Fetcher:
    """Fetches HSL data from HTTPS url and saves it as a local temporary zip file"""

    def __init__(self, data_url=DATA_URL):
        if not data_url:
            raise AttributeError("No data url!")

        self._data_url = data_url

        self.data_file = None

        self._log = logging.getLogger("DataFetcher")

    def fetch(self, skip_fetching=False):
        """Fetcher data zip file and saves it to a temporary location"""

        if skip_fetching:
            self._log.info("skip_fetching set, skipping fetching")
            return

        tmp_file_name = "HSL.zip"

        timeout = 60 # seconds

        with requests.get(self._data_url, stream=False, timeout=timeout) as req:
            with open(tmp_file_name, "wb") as tmp_file:
                tmp_file.write(req.content)
                tmp_file.close()

        os.chmod(tmp_file.name, 0o644)

        self.data_file = tmp_file
        self._log.info("Data file: %s", self.data_file)

import traceback

import requests
from django.conf import settings

from api import models
from api.bro_import import config


class FetchBROIDsError(Exception):
    """Custom exception for errors during BRO IDs fetching."""


class DataImportError(Exception):
    """Custom exception for errors during BRO data import."""


class BulkImporter:
    """Imports bulk data from the BRO for a given KVK and BRO domain.

    It first fetches all BRO id's for the given BRO domain and KVK number.
    Then loops over all id's to import the data if its object.
    Finally, it saves the data in the corresponding datamodel in the database.
    """

    def __init__(self, import_task_instance: models.ImportTask) -> None:
        self.import_task_instance = import_task_instance
        self.bro_domain = self.import_task_instance.bro_domain
        self.kvk_number = self.import_task_instance.kvk_number
        self.data_owner = self.import_task_instance.data_owner

        # Lookup the right importer class to initiate for object
        self.object_importer_class = config.object_importer_mapping[self.bro_domain]

    def run(self) -> None:
        url = self._create_bro_ids_import_url()
        bro_ids = self._fetch_bro_ids(url)

        for bro_id in bro_ids:
            try:
                data_importer = self.object_importer_class(
                    self.bro_domain, bro_id, self.data_owner
                )
                data_importer.run()
            except requests.RequestException as e:
                traceback.print_exc()
                raise DataImportError(f"Error fetching BRO IDs from {url}: {e}") from e

    def _create_bro_ids_import_url(self) -> str:
        """Creates the import url for a given bro object type and kvk combination."""
        bro_domain = self.bro_domain.lower()
        url = f"{settings.BRO_UITGIFTE_SERVICE_URL}/gm/{bro_domain}/v1/bro-ids?bronhouder={self.kvk_number}"
        return url

    def _fetch_bro_ids(self, url) -> list:
        """Fetch BRO IDs from the provided URL.

        Returns:
            list: The fetched BRO IDs.
        """
        try:
            r = requests.get(url)
            r.raise_for_status()
            bro_ids = r.json()["broIds"]

            return bro_ids

        except requests.RequestException as e:
            raise FetchBROIDsError(f"Error fetching BRO IDs from {url}: {e}") from e

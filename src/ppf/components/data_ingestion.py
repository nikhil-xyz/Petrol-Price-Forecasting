import os
import urllib.request as request
import zipfile
from ppf.logging import logger
from ppf.utils.common import get_size
from pathlib import Path
from ppf.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f'Downloaded {filename} to {self.config.local_data_file}')
        else:
            logger.info(f'File {self.config.local_data_file} already exists')

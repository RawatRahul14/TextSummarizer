import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import (DataIngestionConfig)
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"Data has been downloaded at {filename}.")
        else:
            logger.info(f"File has already downloaded of size {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_file_path = self.config.unzip_dir
        os.makedirs(unzip_file_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_file_path)
from textSummarizer.config.configuration import (ConfigurationManager)
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionPipleine:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage: {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionPipleine()
        obj.main()
        logger.info(f">>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
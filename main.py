from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipleine

logger.info("X----------------------X")
STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>> stage: {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionPipleine()
    obj.main()
    logger.info(f">>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("X----------------------X")
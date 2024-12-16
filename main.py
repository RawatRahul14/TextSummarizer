from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipleine
from textSummarizer.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline

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
STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>>>> stage: {STAGE_NAME} started. <<<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage: {STAGE_NAME} completed. <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("X----------------------X")
STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started. <<<<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed. <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
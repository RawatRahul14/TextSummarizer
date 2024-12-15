from textSummarizer.components.data_validation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

STAGE_NAME = "Data Validation"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage: {STAGE_NAME} started. <<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage: {STAGE_NAME} completed. <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
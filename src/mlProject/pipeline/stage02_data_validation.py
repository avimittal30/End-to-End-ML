from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger


Stage_name='Data Validation Stage'

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj=DataValidationPipeline()
        # Run this component of pipeline
        obj.main()
        logger.info(f">>>> Stage {Stage_name} completed <<<<<")

    except Exception as e:
        logger.exception(e)
        raise e


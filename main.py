from mlProject import logger  
from mlProject.pipeline.stage01_data_ingestion import DataIngestionPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.info(f">>> Stage {STAGE_NAME} completed <<<<<<")


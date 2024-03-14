from mlProject import logger  
from mlProject.pipeline.stage01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.info(f">>> Stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_trans = DataTransformationPipeline()
   data_trans.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Training"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME= "Model Evaluation"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_eval = ModelEvaluationPipeline()
   model_eval.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

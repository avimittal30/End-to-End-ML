from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

stage_name="Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {stage_name} started <<<<<<<<<<<<<<")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {stage_name} completed <<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

     
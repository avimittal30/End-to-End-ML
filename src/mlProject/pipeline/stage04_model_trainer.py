from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path


Stage_Name="Model Training"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_training=ModelTrainer(config=model_trainer_config)
        model_training.train()    
                    
if __name__=="__main__":
    try:
          logger.info(f">>>>>> stage {Stage_Name} started <<<<<<<<<<")
          obj=ModelTrainerPipeline() 
          obj.main()
          logger.info(f">>>>> stage {Stage_Name} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

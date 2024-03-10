from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


Stage_Name="Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status=f.read().split(":")[1].strip()

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")
            
        except Exception as e:
            print(e)
            
if __name__=="__main__":
    try:
          logger.info(f">>>>>> stage {Stage_Name} started <<<<<<<<<<")
          obj=DataTransformationPipeline() 
          obj.main()
          logger.info(f">>>>> stage {Stage_Name} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


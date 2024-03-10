import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config

    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)
        data.drop(['Unnamed: 0','RowNumber'], axis=1, inplace=True)
        data.set_index('CustomerId', inplace=True)
        train,test=train_test_split(data)

        train.to_csv( os.path.join(self.config.root_dir,"train.csv"), index=True)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=True)

        logger.info("Splitted data into training and the test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(f"Train Shape :{train.shape}")
        print(f"Test Shape :{test.shape}")
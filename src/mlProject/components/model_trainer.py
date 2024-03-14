import pandas as pd
import os
from mlProject import logger
from sklearn.ensemble import GradientBoostingClassifier
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config=config

    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)

        train_x=train_data.drop([self.config.target_column], axis=1)
        test_x=test_data.drop([self.config.target_column], axis=1)

        train_y=train_data[self.config.target_column]
        test_y=test_data[self.config.target_column]

        xgbc=GradientBoostingClassifier(learning_rate=self.config.learning_rate, max_depth=self.config.max_depth, random_state=10)
        xgbc.fit(train_x, train_y)

        joblib.dump(xgbc, os.path.join(self.config.root_dir, self.config.model_name))
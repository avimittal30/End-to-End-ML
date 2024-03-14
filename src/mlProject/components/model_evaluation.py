from sklearn.metrics import classification_report, recall_score, precision_score, accuracy_score
import os
import pandas as pd
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import read_yaml, create_directories, save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config=config
        
    def eval_metrics(self, actual, pred):
        acc=accuracy_score(actual,pred)
        precision=precision_score(actual,pred)    
        recall=recall_score(actual,pred)
        return acc, precision,recall
    
    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column], axis=1)
        test_y=test_data[[self.config.target_column]]
        
        tracking_url_type_store=urlparse(mlflow.get_artifact_uri()).scheme
        mlflow.set_registry_uri(self.config.mlflow_uri)
        
        if mlflow.active_run():
            mlflow.end_run()

        with mlflow.start_run():
            predicted_class=model.predict(test_x)
            (acc, precision, recall)=self.eval_metrics(test_y,predicted_class)
            
            # Saving metrics as local
            scores={"acc":acc, "precision":precision, "recall":recall}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"precision": precision, "recall": recall, "accuracy": acc })

            if tracking_url_type_store!="file":
                mlflow.sklearn.log_model(model, "mymodel", registered_model_name="XGBClassifier")
            else:
                mlflow.sklearn.log_model(model, "mymodel")
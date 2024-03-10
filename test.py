from pathlib import Path

with open(Path("artifacts/data_validation/status.txt"), "r") as f:
    status=f.read().split(":")[1].strip()

status=="True"



from mlProject.constants import *   
from mlProject.utils.common import read_yaml, create_directories

params_filepath=PARAMS_FILE_PATH
param=read_yaml(params_filepath)


param.GradientBoostingClassifier.max_depth
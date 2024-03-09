from dataclasses import dataclass
from pathlib import Path

# this is to define the return type of variables
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path
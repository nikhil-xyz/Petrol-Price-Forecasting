from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    p: int
    d: int
    q: int


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_path: Path
    predictions_path: Path
    p: int
    d: int
    q: int
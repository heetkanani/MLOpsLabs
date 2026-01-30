from pydantic_settings import BaseSettings
from typing import Optional

class Configurations(BaseSettings):
    MODEL_PATH: str = "../model/iris_model.pkl"
    MODEL_TYPE: str = "DecisionTreeClassifier"

    # config values
    APP_NAME: str = "Iris FastAPI MLOps Lab 1"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # initilaizing default values
    DEFAULT_MAX_DEPTH: int = 3
    DEFAULT_RANDOM_STATE: int = 12
    DEFAULT_TEST_SIZE: float = 0.3

    class Config:
        env_file = ".env"
        case_sensitive = False



from pydantic import BaseModel
from typing import List


# Imported the same models from main.py file
class IrisData(BaseModel):
    petal_length: float
    sepal_length: float
    petal_width: float
    sepal_width: float

class IrisResponse(BaseModel):
    response:int


#adding 5 new models
class ModelRetraining(BaseModel):
    max_depth: int = 3
    random_state: int = 12
    test_size: float = 0.3


class BatchIrisResponse(BaseModel):
    predictions: List[int]

class BatchIrisData(BaseModel):
    data: List[IrisData]

class HealthCheck(BaseModel):
    status: str
    timestamp: str
    model_loaded: bool
    model_path: str
    uptime: str


class ModelInfo(BaseModel):
    model_type: str
    training_date: str
    accuracy: float
    features: List[str]
    classes: List[str]
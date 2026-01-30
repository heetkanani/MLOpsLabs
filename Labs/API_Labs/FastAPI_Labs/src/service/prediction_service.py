from typing import List, Dict, Any
from datetime import datetime
from predict import predict_data
from models import IrisData


class PredictionService:    
    def __init__(self):
        self.prediction_history: List[Dict[str, Any]] = []
    
    def iris_single_predict(self, iris_data: IrisData) -> int:
        features = [[iris_data.sepal_length, iris_data.sepal_width,
                    iris_data.petal_length, iris_data.petal_width]]
        prediction = predict_data(features)
        prediction_value = int(prediction[0])
        self.store_prediction(iris_data, prediction_value)
        
        return prediction_value
    
    def iris_batch_predict(self, batch_data: List[IrisData]) -> List[int]:
        features = []
        for iris_data in batch_data:
            features.append([iris_data.sepal_length, iris_data.sepal_width,
                           iris_data.petal_length, iris_data.petal_width])
        
        predictions = predict_data(features)
        prediction_values = [int(p) for p in predictions]
        
        for i, prediction in enumerate(prediction_values):
            self.store_prediction(batch_data[i], prediction)
        
        return prediction_values
    
    def store_prediction(self, iris_data: IrisData, prediction: int):
        self.prediction_history.append({
            "timestamp": datetime.now().isoformat(),
            "input": iris_data.dict(),
            "prediction": prediction
        })
    
    
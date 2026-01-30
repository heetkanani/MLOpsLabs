import joblib
import os
from datetime import datetime
from typing import Dict, Any

def load_model(model_path: str):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path} oath")
    return joblib.load(model_path)


def get_model_info(model_path: str, model_metrics: Dict[str, Any]) -> Dict[str, Any]:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path} path")
    
    model = load_model(model_path)
    accuracy = model_metrics.get('accuracy', 0.0)
    
    return {
        "model_type": type(model).__name__,
        "training_date": datetime.fromtimestamp(os.path.getmtime(model_path)).isoformat(),
        "accuracy": accuracy,
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "classes": ["setosa", "versicolor", "virginica"]
    }


def save_model(model, model_path: str):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

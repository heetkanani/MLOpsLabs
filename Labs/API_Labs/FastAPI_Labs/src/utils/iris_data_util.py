import numpy as np
from typing import Dict, Any
from data import load_data


def get_iris_data_info() -> Dict[str, Any]:
    X, y = load_data()
    return {
        "dataset_name": "Iris",
        "samples": len(X),
        "features": X.shape[1],
        "classes": len(np.unique(y)),
        "feature_names": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "class_names": ["setosa", "versicolor", "virginica"],
        "data_shape": X.shape
    }
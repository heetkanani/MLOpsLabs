from .all_model_route import router as all_model_route
from .health_check_router import router as health_check_router
from .iris_data_route import router as iris_data_route
from .prediction_route import router as prediction_route

__all__ = [
    "all_model_route",
    "health_check_router",
    "iris_data_route", 
    "prediction_route"
]
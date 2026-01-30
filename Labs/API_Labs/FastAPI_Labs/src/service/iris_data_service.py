from typing import Dict, Any
from utils import get_iris_data_info


class IrisDataService:    
    def get_iris_data_info(self) -> Dict[str, Any]:
        return get_iris_data_info()
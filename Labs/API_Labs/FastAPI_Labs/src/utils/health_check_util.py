import os
from typing import Dict, Any
from datetime import datetime

def get_health_check(model_path: str) -> Dict[str, Any]:
    model_loaded = os.path.exists(model_path)
    
    return {
        "status": "healthy" if model_loaded else "degraded",
        "timestamp": datetime.now().isoformat(),
        "model_loaded": model_loaded,
        "model_path": model_path,
        "uptime": "N/A"  #ignoring upotime for this
    }
import os

def ensure_directory(path):
    """Ensure a directory exists."""
    os.makedirs(path, exist_ok=True)

def get_model_info(model):
    """Get basic information about the model."""
    return {
        'type': type(model).__name__,
        'n_estimators': getattr(model, 'n_estimators', 'N/A'),
        'classes': getattr(model, 'classes_', 'N/A')
    }
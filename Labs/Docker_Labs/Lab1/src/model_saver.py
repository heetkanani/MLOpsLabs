import os
import joblib
from config import MODEL_FILENAME, ARTIFACTS_DIR


def save_model(model, filename=None):
    """Save the trained model to a file."""
    if filename is None:
        filename = MODEL_FILENAME
    
    # Create artifacts directory if it doesn't exist
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    
    # Save model
    filepath = os.path.join(ARTIFACTS_DIR, filename)
    joblib.dump(model, filepath)
    print(f"Model successfullty saved to {filepath}")
    return filepath
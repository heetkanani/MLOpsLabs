from sklearn.ensemble import RandomForestClassifier
from config import N_ESTIMATORS, RANDOM_STATE


def create_model():
    """Create a Random Forest classifier."""
    return RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        random_state=RANDOM_STATE
    )


def train_model(model, X_train, y_train):
    """Train the model on the training data."""
    model.fit(X_train, y_train)
    return model
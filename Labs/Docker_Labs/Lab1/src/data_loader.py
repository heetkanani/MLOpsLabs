from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from config import TEST_SIZE, RANDOM_STATE


def load_data():
    """Load the Iris dataset and return features and target."""
    iris = load_iris()
    return iris.data, iris.target


def split_data(X, y):
    """Split data into training and testing sets."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    return X_train, X_test, y_train, y_test
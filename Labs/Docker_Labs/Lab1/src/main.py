# Import necessary libraries
from data_loader import load_data, split_data
from model_trainer import create_model, train_model
from model_saver import save_model
from utils import get_model_info

if __name__ == '__main__':
    print("*" * 50)
    print("Starting point for teh ML Training Pipeline")
    print("*" * 50)
    
    # Load data
    print("Step 1: Loading Iris dataset")
    X, y = load_data()
    print(f"Loaded {len(X)} samples with {len(X[0])} features")
    
    # Split data
    print("\nStep 2: Splitting data into train/test split")
    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")
    
    # Create and train model
    print("\nStep 3: Creating Random Forest model ")
    model = create_model()
    print(f"Model created: {type(model).__name__}")
    
    print("\nStep 4: Training the model")
    model = train_model(model, X_train, y_train)
    print("Model training completed")
    
    # Save model
    print("\nStep 5: Saving the model")
    model_path = save_model(model)
    
    # Print summary
    print("*" * 50)
    print("Training Pipeline Summary :")
    print("*" * 50)
    model_info = get_model_info(model)

    print(f"Model Type: {model_info['type']}")
    print(f"Number of Estimators: {model_info['n_estimators']}")
    print(f"Number of Classes: {len(model_info['classes'])}")
    print(f"Model saved to: {model_path}")

    print("*" * 50)
    print("The model training was successful!")
    print("*" * 50)
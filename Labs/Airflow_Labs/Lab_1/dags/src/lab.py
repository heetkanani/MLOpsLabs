import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.neighbors import NearestNeighbors
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    """
    Loads data from a CSV file, serializes it, and returns the serialized data.

    Returns:
        bytes: Serialized data.
    """
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/file.csv"))
    serialized_data = pickle.dumps(df)
    
    return serialized_data
    

def data_preprocessing(data):
    """
    Deserializes data, performs data preprocessing with StandardScaler for DBSCAN,
    and returns serialized clustered data along with original dataframe.

    Args:
        data (bytes): Serialized data to be deserialized and processed.

    Returns:
        bytes: Serialized tuple of (scaled_data, original_df, scaler).
    """
    df = pickle.loads(data)
    df = df.dropna()
    
    # Select features for clustering
    clustering_data = df[["BALANCE", "PURCHASES", "CREDIT_LIMIT"]]
    
    # Use StandardScaler for DBSCAN (works better than MinMaxScaler for density-based methods)
    scaler = StandardScaler()
    clustering_data_scaled = scaler.fit_transform(clustering_data)
    
    # Package data for next step
    processed_data = (clustering_data_scaled, df, scaler, clustering_data.columns.tolist())
    clustering_serialized_data = pickle.dumps(processed_data)
    
    return clustering_serialized_data


def find_optimal_eps(data, min_samples=5):
    """
    Find optimal eps value using k-nearest neighbors.
    
    Args:
        data: Scaled data for clustering
        min_samples: Minimum samples for DBSCAN
    
    Returns:
        float: Suggested eps value
    """
    # Calculate nearest neighbors
    neighbors = NearestNeighbors(n_neighbors=min_samples)
    neighbors_fit = neighbors.fit(data)
    distances, indices = neighbors_fit.kneighbors(data)
    
    # Sort distances
    distances = np.sort(distances[:, min_samples-1], axis=0)
    
    # Find the "elbow" point (you might want to visualize this)
    # Using a simple heuristic: point with maximum curvature
    diff1 = np.diff(distances.flatten())
    diff2 = np.diff(diff1)
    
    # Get the point with maximum second derivative
    if len(diff2) > 0:
        elbow_idx = np.argmax(diff2) + 2
        optimal_eps = distances.flatten()[elbow_idx]
    else:
        # Fallback to a percentile-based approach
        optimal_eps = np.percentile(distances, 90)
    
    return optimal_eps


def build_save_model(data, filename):
    """
    Builds a DBSCAN clustering model with hyperparameter tuning,
    saves it to a file, and returns cluster information.

    Args:
        data (bytes): Serialized data for clustering.
        filename (str): Name of the file to save the clustering model.

    Returns:
        dict: Dictionary containing clustering metrics and parameters.
    """
    # Unpack the processed data
    clustering_data_scaled, original_df, scaler, feature_names = pickle.loads(data)
    
    # Hyperparameter tuning for DBSCAN
    min_samples_range = [3, 5, 7, 10]
    best_score = -1
    best_params = {}
    best_model = None
    
    for min_samples in min_samples_range:
        # Find optimal eps for this min_samples value
        eps = find_optimal_eps(clustering_data_scaled, min_samples)
        
        # Train DBSCAN
        dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean', n_jobs=-1)
        clusters = dbscan.fit_predict(clustering_data_scaled)
        
        # Check if we have at least 2 clusters (excluding noise)
        n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
        
        if n_clusters >= 2:
            # Calculate silhouette score (excluding noise points)
            mask = clusters != -1
            if mask.sum() > 0:
                score = silhouette_score(clustering_data_scaled[mask], clusters[mask])
                
                if score > best_score:
                    best_score = score
                    best_params = {'eps': eps, 'min_samples': min_samples}
                    best_model = dbscan
    
    # Use best model or fallback to default parameters
    if best_model is None:
        # Fallback to default parameters if no good clustering found
        eps = 0.5
        min_samples = 5
        best_model = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean', n_jobs=-1)
        clusters = best_model.fit_predict(clustering_data_scaled)
        best_params = {'eps': eps, 'min_samples': min_samples}
    else:
        clusters = best_model.labels_
    
    # Calculate clustering metrics
    n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
    n_noise = list(clusters).count(-1)
    
    # Prepare model package with scaler and parameters
    model_package = {
        'model': best_model,
        'scaler': scaler,
        'params': best_params,
        'feature_names': feature_names,
        'n_clusters': n_clusters,
        'n_noise_points': n_noise,
        'silhouette_score': best_score if best_score > -1 else None
    }
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, filename)
    
    # Save the model package
    with open(output_path, 'wb') as f:
        pickle.dump(model_package, f)
    
    # Return metrics for monitoring
    metrics = {
        'n_clusters': n_clusters,
        'n_noise_points': n_noise,
        'eps': best_params['eps'],
        'min_samples': best_params['min_samples'],
        'silhouette_score': best_score if best_score > -1 else None,
        'total_points': len(clusters)
    }
    
    return metrics


def evaluate_model(filename, metrics):
    """
    Loads a saved DBSCAN clustering model and evaluates it on test data.

    Args:
        filename (str): Name of the file containing the saved clustering model.
        metrics (dict): Dictionary containing training metrics.

    Returns:
        dict: Evaluation results including predictions and cluster assignments.
    """
    output_path = os.path.join(os.path.dirname(__file__), "../model", filename)
    
    # Load the saved model package
    with open(output_path, 'rb') as f:
        model_package = pickle.load(f)
    
    model = model_package['model']
    scaler = model_package['scaler']
    feature_names = model_package['feature_names']
    
    # Load test data
    df_test = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/test.csv"))
    
    # Preprocess test data
    test_features = df_test[feature_names]
    test_features_scaled = scaler.transform(test_features)
    
    # For DBSCAN, we need to find the nearest cluster for new points
    # since DBSCAN doesn't have a direct predict method
    # We'll use the core samples from training to assign new points
    
    # Get core sample indices
    core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
    core_samples_mask[model.core_sample_indices_] = True
    
    # For each test point, find the nearest core sample and assign its cluster
    from sklearn.neighbors import KNeighborsClassifier
    
    if len(model.core_sample_indices_) > 0:
        # Train a KNN classifier on core samples
        knn = KNeighborsClassifier(n_neighbors=1)
        core_samples = model.components_
        core_labels = model.labels_[model.core_sample_indices_]
        knn.fit(core_samples, core_labels)
        
        # Predict clusters for test data
        predictions = knn.predict(test_features_scaled)
    else:
        # If no core samples, all points are noise
        predictions = np.array([-1] * len(test_features_scaled))
    
    # Prepare results
    results = {
        'predictions': predictions.tolist(),
        'n_clusters_found': len(set(predictions)) - (1 if -1 in predictions else 0),
        'n_noise_points': list(predictions).count(-1),
        'training_metrics': metrics,
        'model_params': model_package['params']
    }
    
    # Print summary
    print(f"DBSCAN Clustering Results:")
    print(f"- Optimal eps: {model_package['params']['eps']:.4f}")
    print(f"- Optimal min_samples: {model_package['params']['min_samples']}")
    print(f"- Training clusters: {metrics['n_clusters']}")
    print(f"- Training noise points: {metrics['n_noise_points']}/{metrics['total_points']}")
    print(f"- Test predictions: {len(predictions)} samples")
    print(f"- Test cluster distribution: {dict(zip(*np.unique(predictions, return_counts=True)))}")
    
    return results
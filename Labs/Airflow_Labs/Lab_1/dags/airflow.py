# Import necessary libraries and modules
import os
import logging
import pickle
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from src.lab import load_data, data_preprocessing, build_save_model, load_model_elbow
from airflow import configuration as conf

logger = logging.getLogger("airflow.task")

# NOTE:
# In Airflow 3.x, enabling XCom pickling should be done via environment variable:
# export AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
# The old airflow.configuration API is deprecated.
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "model.sav")
DBSCAN_MODEL_PATH = os.path.join(MODEL_DIR,"dbscan_model.pkl")

conf.set('core', 'enable_xcom_pickling', 'True')

def build_dbscan_model(data, kmeans_output):
    """
    Build a DBSCAN model.
    Uses the optimal cluster count from KMeans elbow to set min_samples.
    """
    from sklearn.cluster import DBSCAN
    from sklearn.metrics import silhouette_score

    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(data)

    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    logger.info(f"DBSCAN found {n_clusters} clusters and {n_noise} noise points")

    if n_clusters > 1:
        score = silhouette_score(data, labels)

    with open(DBSCAN_MODEL_PATH, 'wb') as f:
        pickle.dump(dbscan, f)
    logger.info(f"DBSCAN model saved to {DBSCAN_MODEL_PATH}")

    return labels


# Define default arguments for your DAG
default_args = {
    'owner': 'Heet Kanani',
    'start_date': datetime(2026, 2, 25),
    'retries': 0,  # Number of retries in case of task failure
    'retry_delay': timedelta(minutes=5),  # Delay before retries
}

# Create a DAG instance named 'Airflow_Lab1' with the defined default arguments
with DAG(
    'Heet_Kanani_Airflow_Lab1',
    default_args=default_args,
    description='Dag example for Lab 1 of Airflow series',
    schedule_interval='@weekly',
    catchup=False,
    tags=['ml', 'clustering', 'lab1'],
) as dag:

    # Task to load data, calls the 'load_data' Python function
    load_data_task = PythonOperator(
        task_id='load_data_task',
        python_callable=load_data,
    )

    # Task to perform data preprocessing, depends on 'load_data_task'
    data_preprocessing_task = PythonOperator(
        task_id='data_preprocessing_task',
        python_callable=data_preprocessing,
        op_args=[load_data_task.output],
    )

    # Task to build and save a model, depends on 'data_preprocessing_task'
    build_save_model_task = PythonOperator(
        task_id='build_save_model_task',
        python_callable=build_save_model,
        op_args=[data_preprocessing_task.output, MODEL_PATH],
    )

    # Task to load a model using the 'load_model_elbow' function, depends on 'build_save_model_task'
    load_model_task = PythonOperator(
        task_id='load_model_task',
        python_callable=load_model_elbow,
        op_args=[MODEL_PATH, build_save_model_task.output],
    )

    # Task to build DBSCAN model
    build_dbscan_task = PythonOperator(
        task_id='build_dbscan_task',
        python_callable=build_dbscan_model,
        op_args=[data_preprocessing_task.output, load_model_task.output],
    )

    # Set task dependencies
    load_data_task >> data_preprocessing_task >> build_save_model_task >> load_model_task >> build_dbscan_task

# If this script is run directly, allow command-line interaction with the DAG
if __name__ == "__main__":
    dag.test()
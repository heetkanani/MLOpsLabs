# MLOPS - Lab1 - Overall Lab 4

This Lab trains a Random Forest classifier on the Iris dataset using Scikit-Learn and provides a REST API.

## Project Structure

```
Lab1/
├── src/
│   ├── main.py          # Main entry point for training pipeline
│   ├── config.py        # Configuration constants
│   ├── data_loader.py   # Data loading utilities
│   ├── model_trainer.py # Model training utilities
│   ├── model_saver.py   # Model saving utilities
│   ├── utils.py         # Utility functions
│   └── requirements.txt # Python dependencies
├── Dockerfile.train     # Dockerfile for training service
├── dockerfile           # Original Dockerfile - API
├── docker-compose.yml   # Docker Compose configuration
├── api_server.py        # Flask API server for model inference
└── artifacts/           # Output directory for trained models
```

## Lab 1 Setup and steps to ru the lab

### Using Docker Compose

1. **Build and run the training service:**
```bash
docker compose run --rm train
```

This will:
- Build the training Docker image
- Run the training pipeline
- Save the model to `./artifacts/iris_model.pkl`

2. **Start the API service:**
```bash
docker compose up -d api
```

This will:
- Build the API Docker image
- Start the Flask API server on port 5000
- The API will be available at `http://localhost:5000`

### Using Docker directly

**Training service:**
```bash
# Build the training image
docker build -f Dockerfile.train -t lab4-train .

# Run the training container
docker run --rm -v ${PWD}/artifacts:/app/artifacts lab4-train
```

**API service:**
```bash
# Build the API image
docker build -f Dockerfile.api -t lab4-docker .

# Run the API container
docker run --rm -p 5000:5000 -v ${PWD}/artifacts:/app/artifacts lab4-docker
```

## API Usage

### Health Check

```bash
curl http://localhost:5000/health
```

Response:
```json
{"status": "healthy"}
```

This is used to check is the api service is up and running

### Model Prediction

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

This gives the model output
**Note:** The features array should contain 4 values (sepal length, sepal width, petal length, petal width).

## Services uswd in docker file

### Train Service
- Builds from `Dockerfile.train`
- Runs the complete ML training pipeline
- Saves the trained model to `./artifacts/iris_model.pkl`

### API Service
- Builds from `dockerfile`
- Provides REST API endpoints for model inference
- Exposes port 5000
- Depends on the train service to ensure model exists

## Output
Once the training container finishes successfully, it saves the model to `./artifacts/iris_model.pkl`. The API service uses this model file for predictions.
from fastapi import FastAPI, status, HTTPException
from config import Configurations
from routes import prediction_route, all_model_route, health_check_router, iris_data_route
# from pydantic import BaseModel
# from predict import predict_data

configurations = Configurations()
app = FastAPI(
    title=configurations.APP_NAME,
    version=configurations.APP_VERSION,
    description="ML Fast API lab using Iris Dataset"
)

app.include_router(all_model_route)
app.include_router(health_check_router)
app.include_router(iris_data_route)
app.include_router(prediction_route)


@app.get("/")
async def root():
    return {
        "message": "ML Fast API lab using Iris Datase",
        "version": configurations.APP_VERSION,
        "docs": "/docs",
        "health": "/health"
    }

# all the below endpoints are addded in different folder structure 
# class IrisData(BaseModel):
#     petal_length: float
#     sepal_length: float
#     petal_width: float
#     sepal_width: float

# class IrisResponse(BaseModel):
#     response:int

# @app.get("/", status_code=status.HTTP_200_OK)
# async def health_ping():
#     return {"status": "healthy"}

# @app.post("/predict", response_model=IrisResponse)
# async def predict_iris(iris_features: IrisData):
#     try:
#         features = [[iris_features.sepal_length, iris_features.sepal_width,
#                     iris_features.petal_length, iris_features.petal_width]]

#         prediction = predict_data(features)
#         return IrisResponse(response=int(prediction[0]))
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    


    

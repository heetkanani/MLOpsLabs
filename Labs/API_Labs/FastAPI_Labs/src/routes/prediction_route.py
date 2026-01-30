from fastapi import APIRouter, HTTPException, Query
from models import IrisData, IrisResponse, BatchIrisData, BatchIrisResponse
from service import PredictionService

router = APIRouter(prefix="/predict", tags=["predictions"])
prediction_service = PredictionService()


@router.post("/single", response_model=IrisResponse)
async def iris_single_predict(iris_features: IrisData):
    try:
        prediction = prediction_service.iris_single_predict(iris_features)
        return IrisResponse(response=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/batch", response_model=BatchIrisResponse)
async def iris_batch_predict(batch_data: BatchIrisData):
    try:
        predictions = prediction_service.iris_batch_predict(batch_data.data)
        return BatchIrisResponse(predictions=predictions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from models import ModelInfo, ModelRetraining
from service import AllModelService
from config import Configurations

router = APIRouter(prefix="/model", tags=["model"])

configurations = Configurations()
model_service = AllModelService(configurations.MODEL_PATH)


@router.get("/info", response_model=ModelInfo)
async def get_model_info():
    try:
        info = model_service.get_model_info()
        return ModelInfo(**info)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/retraining")
async def model_retraining(retrain_params: ModelRetraining):
    try:
        result = model_service.model_retraining(retrain_params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/metrics")
async def get_model_metrics():
    try:
        return model_service.get_model_metrics()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download")
async def model_download():
    try:
        return FileResponse(
            path=configurations.MODEL_PATH,
            filename="iris_model.pkl",
            media_type="application/octet-stream"
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
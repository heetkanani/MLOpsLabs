from fastapi import APIRouter, status, HTTPException  
from models import HealthCheck
from utils import get_health_check
from config import Configurations

router = APIRouter(prefix="/health", tags=["health"])
configurations = Configurations()


@router.get("/", status_code=status.HTTP_200_OK)
async def single_health_check():
    return {"status": "healthy"}


@router.get("/detailcheck", response_model=HealthCheck)
async def detail_health_check():
    try:
        health_data = get_health_check(configurations.MODEL_PATH)
        return HealthCheck(**health_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
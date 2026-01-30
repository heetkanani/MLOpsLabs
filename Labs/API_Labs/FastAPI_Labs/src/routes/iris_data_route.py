from fastapi import APIRouter, HTTPException
from service import IrisDataService

router = APIRouter(prefix="/irisdata", tags=["data"])
iris_data_service = IrisDataService()

@router.get("/info")
async def get_iris_data_info():
    try:
        return iris_data_service.get_iris_data_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
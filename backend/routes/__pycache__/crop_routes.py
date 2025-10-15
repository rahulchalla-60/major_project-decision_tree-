from fastapi import APIRouter, HTTPException
from services.crop_service import get_crop_profile, get_ticker_data

router = APIRouter(prefix="/commodity", tags=["Commodity"])

@router.get("/{name}")
def crop_profile(name: str):
    try:
        return get_crop_profile(name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/ticker/{item}/{number}")
def ticker(item: int, number: int):
    try:
        return get_ticker_data(item, number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# app/routes/forecast_routes.py

from fastapi import APIRouter
from models.commodity_model import Commodity
from models.crop_data import commodity_dict
from services import forecast_service

router = APIRouter(prefix="/forecast", tags=["Forecast"])

commodity_list = []

@router.on_event("startup")
def load_commodities():
    global commodity_list
    for name, path in commodity_dict.items():
        commodity_list.append(Commodity(path))
    print(f"✅ Loaded {len(commodity_list)} commodities successfully!")

# Top/Bottom 5
@router.get("/top5")
def get_top5():
    return forecast_service.TopFiveWinners(commodity_list)

@router.get("/bottom5")
def get_bottom5():
    return forecast_service.TopFiveLosers(commodity_list)

# Six months forecast
@router.get("/sixmonths")
def get_sixmonths():
    return forecast_service.SixMonthsForecast(commodity_list)

# Current month price
@router.get("/current/{name}")
def get_current(name: str):
    return {"price": forecast_service.CurrentMonth(commodity_list, name)}

# Twelve months forecast
@router.get("/twelve/{name}")
def get_twelve(name: str):
    max_crop, min_crop, forecast = forecast_service.TwelveMonthsForecast(commodity_list, name)
    prev = forecast_service.TwelveMonthPrevious(commodity_list, name)
    return {
        "max_crop": max_crop,
        "min_crop": min_crop,
        "forecast": forecast,
        "previous": prev
    }

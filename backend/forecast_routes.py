from fastapi import APIRouter
import commodity_model
import forecast_service
import crop_data
import crops

router = APIRouter(prefix="/forecast", tags=["Forecast"])
commodity_list = []

@router.on_event("startup")
def load_commodities():
    global commodity_list
    for name, path in crop_data.commodity_dict.items():
        commodity_list.append(commodity_model.Commodity(path))
    print(f"✅ Loaded {len(commodity_list)} commodities!")

@router.get("/top5")
def get_top5():
    return forecast_service.TopFiveWinners(commodity_list)

@router.get("/bottom5")
def get_bottom5():
    return forecast_service.TopFiveLosers(commodity_list)

@router.get("/sixmonths")
def get_sixmonths():
    return forecast_service.SixMonthsForecast(commodity_list)

@router.get("/current/{name}")
def get_current(name: str):
    return {"price": forecast_service.CurrentMonth(commodity_list, name)}

@router.get("/twelve/{name}")
def get_twelve(name: str):
    max_crop, min_crop, forecast = forecast_service.TwelveMonthsForecast(commodity_list, name)
    prev = forecast_service.TwelveMonthPrevious(commodity_list, name)
    crop_data_info = crops.crop(name.lower())
    return {
        "max_crop": max_crop,
        "min_crop": min_crop,
        "forecast": forecast,
        "previous": prev,
        "image_url": crop_data_info[0],
        "prime_loc": crop_data_info[1],
        "type_c": crop_data_info[2],
        "export": crop_data_info[3]
    }

@router.get("/ticker/{item}/{number}")
def ticker(item: int, number: int):
    data = forecast_service.SixMonthsForecast(commodity_list)
    if 0 <= number < len(data) and 0 <= item < len(data[number]):
        value = data[number][item]
        return {"value": value}
    return {"error": "Index out of range"}

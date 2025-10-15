import crops
from services.forecast_service import (
    TwelveMonthsForecast,
    TwelveMonthPrevious,
    CurrentMonth,
    SixMonthsForecast
)

def get_crop_profile(name: str):
    max_crop, min_crop, forecast_crop_values = TwelveMonthsForecast(name)
    prev_crop_values = TwelveMonthPrevious(name)
    forecast_x = [i[0] for i in forecast_crop_values]
    forecast_y = [i[1] for i in forecast_crop_values]
    previous_x = [i[0] for i in prev_crop_values]
    previous_y = [i[1] for i in prev_crop_values]
    current_price = CurrentMonth(name)
    crop_data = crops.crop(name)

    context = {
        "name": name,
        "max_crop": max_crop,
        "min_crop": min_crop,
        "forecast_values": forecast_crop_values,
        "forecast_x": forecast_x,
        "forecast_y": forecast_y,
        "previous_values": prev_crop_values,
        "previous_x": previous_x,
        "previous_y": previous_y,
        "current_price": current_price,
        "image_url": crop_data[0],
        "prime_loc": crop_data[1],
        "type_c": crop_data[2],
        "export": crop_data[3],
    }
    return context


def get_ticker_data(item: int, number: int):
    data = SixMonthsForecast()
    context = str(data[number][item])

    if item in [2, 5]:
        context = '₹' + context
    elif item in [3, 6]:
        context = context + '%'

    return {"value": context}

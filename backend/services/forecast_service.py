# app/services/forecast_service.py

from datetime import datetime
from app.models.crop_data import annual_rainfall, base

# ---------- TOP/BOTTOM 5 ----------
def TopFiveWinners(commodity_list):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = annual_rainfall[prev_month - 1]

    current_preds, prev_preds, change = [], [], []

    for i in commodity_list:
        curr = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        prev = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        current_preds.append(curr)
        prev_preds.append(prev)
        change.append((((curr - prev) * 100 / prev), commodity_list.index(i)))

    change.sort(reverse=True)
    result = []
    for j in range(5):
        perc, i = change[j]
        name = commodity_list[i].getCropName()
        result.append({
            "name": name,
            "price": round((current_preds[i] * base[name.capitalize()]) / 100, 2),
            "change": round(perc, 2)
        })
    return result


def TopFiveLosers(commodity_list):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = annual_rainfall[prev_month - 1]

    current_preds, prev_preds, change = [], [], []

    for i in commodity_list:
        curr = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        prev = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        current_preds.append(curr)
        prev_preds.append(prev)
        change.append((((curr - prev) * 100 / prev), commodity_list.index(i)))

    change.sort()
    result = []
    for j in range(5):
        perc, i = change[j]
        name = commodity_list[i].getCropName()
        result.append({
            "name": name,
            "price": round((current_preds[i] * base[name.capitalize()]) / 100, 2),
            "change": round(perc, 2)
        })
    return result

# ---------- SIX MONTH FORECAST ----------
def SixMonthsForecastHelper(commodity, name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name = name.lower()
    month_with_year = []

    for i in range(1, 7):
        if current_month + i <= 12:
            month_with_year.append((current_month + i, current_year, annual_rainfall[current_month + i - 1]))
        else:
            month_with_year.append((current_month + i - 12, current_year + 1, annual_rainfall[current_month + i - 13]))

    wpis = []
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    for m, y, r in month_with_year:
        current_predict = commodity.getPredictedValue([float(m), y, r])
        wpis.append(current_predict)

    crop_price = []
    for i in range(len(wpis)):
        m, y, r = month_with_year[i]
        x = datetime(y, m, 1).strftime("%b %y")
        crop_price.append([x, round((wpis[i] * base[name.capitalize()]) / 100, 2),
                           round(((wpis[i] - current_wpi) * 100) / current_wpi, 2)])
    return crop_price


def SixMonthsForecast(commodity_list):
    result = {}
    for i in commodity_list:
        name = i.getCropName()
        result[name] = SixMonthsForecastHelper(i, name)
    return result

# ---------- CURRENT MONTH PRICE ----------
def CurrentMonth(commodity_list, name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name_lower = name.lower()
    commodity = next((c for c in commodity_list if c.getCropName().lower() == name_lower), None)
    if commodity:
        current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
        return round((base[name.capitalize()] * current_wpi) / 100, 2)
    return None

# ---------- 12 MONTH FORECAST ----------
def TwelveMonthsForecast(commodity_list, name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = annual_rainfall[current_month - 1]
    name_lower = name.lower()
    commodity = next((c for c in commodity_list if c.getCropName().lower() == name_lower), commodity_list[0])

    month_with_year = []
    for i in range(1, 13):
        if current_month + i <= 12:
            month_with_year.append((current_month + i, current_year, annual_rainfall[current_month + i - 1]))
        else:
            month_with_year.append((current_month + i - 12, current_year + 1, annual_rainfall[current_month + i - 13]))

    wpis = []
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    max_value, min_value = 0, 999999
    max_index, min_index = 0, 0

    for idx, (m, y, r) in enumerate(month_with_year):
        val = commodity.getPredictedValue([float(m), y, r])
        wpis.append(val)
        if val > max_value:
            max_value = val
            max_index = idx
        if val < min_value:
            min_value = val
            min_index = idx

    crop_price = []
    for idx, (m, y, r) in enumerate(month_with_year):
        x = datetime(y, m, 1).strftime("%b %y")
        crop_price.append([x, round((wpis[idx] * base[name.capitalize()]) / 100, 2),
                           round(((wpis[idx] - current_wpi) * 100) / current_wpi, 2)])

    max_crop = [datetime(month_with_year[max_index][1], month_with_year[max_index][0], 1).strftime("%b %y"),
                round((max_value * base[name.capitalize()]) / 100, 2)]
    min_crop = [datetime(month_with_year[min_index][1], month_with_year[min_index][0], 1).strftime("%b %y"),
                round((min_value * base[name.capitalize()]) / 100, 2)]

    return max_crop, min_crop, crop_price

# ---------- 12 MONTH PREVIOUS ----------
def TwelveMonthPrevious(commodity_list, name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    name_lower = name.lower()
    commodity = next((c for c in commodity_list if c.getCropName().lower() == name_lower), commodity_list[0])

    month_with_year = []
    for i in range(1, 13):
        if current_month - i >= 1:
            month_with_year.append((current_month - i, current_year, annual_rainfall[current_month - i - 1]))
        else:
            month_with_year.append((current_month - i + 12, current_year - 1, annual_rainfall[current_month - i + 11]))

    crop_price = []
    for m, y, r in month_with_year:
        val = commodity.getPredictedValue([float(m), 2013, r])
        crop_price.append([datetime(y, m, 1).strftime("%b %y"),
                           round((val * base[name.capitalize()]) / 100, 2)])

    crop_price.reverse()
    return crop_price

from datetime import datetime
import crop_data
from crops import crop

# Top/Bottom 5 Winners & Losers
def TopFiveWinners(commodity_list):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = crop_data.annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = crop_data.annual_rainfall[prev_month - 1]
    current_month_prediction, prev_month_prediction, change = [], [], []

    for i in commodity_list:
        curr = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        prev = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        current_month_prediction.append(curr)
        prev_month_prediction.append(prev)
        change.append((((curr - prev) * 100 / prev), commodity_list.index(i)))

    change.sort(reverse=True)
    to_send = []
    for j in range(5):
        perc, idx = change[j]
        name = commodity_list[idx].getCropName().split('/')[0]
        to_send.append([name, round((current_month_prediction[idx] * crop_data.base[name.capitalize()]) / 100, 2), round(perc, 2)])
    return to_send

def TopFiveLosers(commodity_list):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = crop_data.annual_rainfall[current_month - 1]
    prev_month = current_month - 1
    prev_rainfall = crop_data.annual_rainfall[prev_month - 1]
    current_month_prediction, prev_month_prediction, change = [], [], []

    for i in commodity_list:
        curr = i.getPredictedValue([float(current_month), current_year, current_rainfall])
        prev = i.getPredictedValue([float(prev_month), current_year, prev_rainfall])
        current_month_prediction.append(curr)
        prev_month_prediction.append(prev)
        change.append((((curr - prev) * 100 / prev), commodity_list.index(i)))

    change.sort()
    to_send = []
    for j in range(5):
        perc, idx = change[j]
        name = commodity_list[idx].getCropName().split('/')[0]
        to_send.append([name, round((current_month_prediction[idx] * crop_data.base[name.capitalize()]) / 100, 2), round(perc, 2)])
    return to_send

def SixMonthsForecast(commodity_list):
    from datetime import datetime
    month1, month2, month3, month4, month5, month6 = [], [], [], [], [], []
    for i in commodity_list:
        crop_forecast = SixMonthsForecastHelper(i)
        for k, val in enumerate(crop_forecast):
            price, change, name, time = val
            if k == 0: month1.append((price, change, name, time))
            elif k == 1: month2.append((price, change, name, time))
            elif k == 2: month3.append((price, change, name, time))
            elif k == 3: month4.append((price, change, name, time))
            elif k == 4: month5.append((price, change, name, time))
            elif k == 5: month6.append((price, change, name, time))
    return [month1, month2, month3, month4, month5, month6]

def SixMonthsForecastHelper(commodity):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = crop_data.annual_rainfall[current_month - 1]
    name = commodity.getCropName().split('/')[0].lower()
    month_with_year = []
    for i in range(1, 7):
        if current_month + i <= 12:
            month_with_year.append((current_month + i, current_year, crop_data.annual_rainfall[current_month + i - 1]))
        else:
            month_with_year.append((current_month + i - 12, current_year + 1, crop_data.annual_rainfall[current_month + i - 13]))
    wpis, change = [], []
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    for m, y, r in month_with_year:
        val = commodity.getPredictedValue([float(m), y, r])
        wpis.append(val)
        change.append(((val - current_wpi) * 100) / current_wpi)
    crop_price = []
    for i, (m, y, r) in enumerate(month_with_year):
        x = datetime(y, m, 1).strftime("%b %y")
        crop_price.append([x, round((wpis[i] * crop_data.base[name.capitalize()]) / 100, 2), round(change[i], 2), name])
    return crop_price

def CurrentMonth(commodity_list, name):
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_rainfall = crop_data.annual_rainfall[current_month - 1]
    name = name.lower()
    commodity = next((c for c in commodity_list if name in c.getCropName().lower()), commodity_list[0])
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, current_rainfall])
    return round((current_wpi * crop_data.base[name.capitalize()]) / 100, 2)

def TwelveMonthsForecast(commodity_list, name):
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    name_lower = name.lower()
    commodity = next((c for c in commodity_list if name_lower in c.getCropName().lower()), commodity_list[0])
    month_with_year = []
    for i in range(1, 13):
        if current_month + i <= 12:
            month_with_year.append((current_month + i, current_year, crop_data.annual_rainfall[current_month + i - 1]))
        else:
            month_with_year.append((current_month + i - 12, current_year + 1, crop_data.annual_rainfall[current_month + i - 13]))

    max_val, min_val = 0, float('inf')
    max_index = min_index = 0
    wpis, change = [], []
    current_wpi = commodity.getPredictedValue([float(current_month), current_year, crop_data.annual_rainfall[current_month - 1]])
    for idx, (m, y, r) in enumerate(month_with_year):
        val = commodity.getPredictedValue([float(m), y, r])
        wpis.append(val)
        change.append(((val - current_wpi) * 100) / current_wpi)
        if val > max_val: max_val, max_index = val, idx
        if val < min_val: min_val, min_index = val, idx

    crop_price = []
    for i, (m, y, r) in enumerate(month_with_year):
        x = datetime(y, m, 1).strftime("%b %y")
        crop_price.append([x, round((wpis[i] * crop_data.base[name.capitalize()]) / 100, 2), round(change[i], 2)])
    max_crop = [datetime(month_with_year[max_index][1], month_with_year[max_index][0], 1).strftime("%b %y"),
                round((max_val * crop_data.base[name.capitalize()]) / 100, 2)]
    min_crop = [datetime(month_with_year[min_index][1], month_with_year[min_index][0], 1).strftime("%b %y"),
                round((min_val * crop_data.base[name.capitalize()]) / 100, 2)]
    return max_crop, min_crop, crop_price

def TwelveMonthPrevious(commodity_list, name):
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    name_lower = name.lower()
    commodity = next((c for c in commodity_list if name_lower in c.getCropName().lower()), commodity_list[0])
    month_with_year = []
    for i in range(1, 13):
        if current_month - i >= 1:
            month_with_year.append((current_month - i, current_year, crop_data.annual_rainfall[current_month - i - 1]))
        else:
            month_with_year.append((current_month - i + 12, current_year - 1, crop_data.annual_rainfall[current_month - i + 11]))
    crop_price = []
    for m, y, r in month_with_year:
        val = commodity.getPredictedValue([float(m), 2013, r])
        crop_price.append([datetime(y, m, 1).strftime("%b %y"), round((val * crop_data.base[name.capitalize()]) / 100, 2)])
    return list(reversed(crop_price))

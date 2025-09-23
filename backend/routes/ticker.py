from flask import Blueprint
from flask_cors import cross_origin
from services.forecast_service import SixMonthsForecast
from models.commodity import commodity_list

ticker_bp = Blueprint('ticker', __name__)

@ticker_bp.route('/ticker/<item>/<number>')
@cross_origin(origin='localhost', headers=['Content-Type','Authorization'])
def ticker(item, number):
    n = int(number)
    i = int(item)
    data = SixMonthsForecast(commodity_list)
    context = str(data[n][i])

    if i == 2 or i == 5:
        context = '₹' + context
    elif i == 3 or i == 6:
        context = context + '%'

    return context

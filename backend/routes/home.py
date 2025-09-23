from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "Welcome to the Home Page"

from services.forecast_service import TopFiveWinners, TopFiveLosers, SixMonthsForecast

def create_home_bp(commodity_list):
    home_bp = Blueprint("home", __name__)

    @home_bp.route('/')
    def index():
        context = {
            "top5": TopFiveWinners(commodity_list),
            "bottom5": TopFiveLosers(commodity_list),
            "sixmonths": SixMonthsForecast(commodity_list)
        }
        return render_template('index.html', context=context)

    return home_bp

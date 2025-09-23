# backend/config.py
class Config:
    COMMODITY_DICT = {
        "arhar": "static/Arhar.csv",
        "bajra": "static/Bajra.csv",
        "barley": "static/Barley.csv",
        "copra": "static/Copra.csv",
        "cotton": "static/Cotton.csv",
        "sesamum": "static/Sesamum.csv",
        "gram": "static/Gram.csv",
        "groundnut": "static/Groundnut.csv",
        "jowar": "static/Jowar.csv",
        "maize": "static/Maize.csv",
        "masoor": "static/Masoor.csv",
        "moong": "static/Moong.csv",
        "niger": "static/Niger.csv",
        "paddy": "static/Paddy.csv",
        "ragi": "static/Ragi.csv",
        "rape": "static/Rape.csv",
        "jute": "static/Jute.csv",
        "safflower": "static/Safflower.csv",
        "soyabean": "static/Soyabean.csv",
        "sugarcane": "static/Sugarcane.csv",
        "sunflower": "static/Sunflower.csv",
        "urad": "static/Urad.csv",
        "wheat": "static/Wheat.csv"
    }

    ANNUAL_RAINFALL = [29, 21, 37.5, 30.7, 52.6, 150, 299, 251.7, 179.2, 70.5, 39.8, 10.9]

    BASE = {
        "Paddy": 1245.5,
        "Arhar": 3200,
        "Bajra": 1175,
        "Barley": 980,
        "Copra": 5100,
        "Cotton": 3600,
        "Sesamum": 4200,
        "Gram": 2800,
        "Groundnut": 3700,
        "Jowar": 1520,
        "Maize": 1175,
        "Masoor": 2800,
        "Moong": 3500,
        "Niger": 3500,
        "Ragi": 1500,
        "Rape": 2500,
        "Jute": 1675,
        "Safflower": 2500,
        "Soyabean": 2200,
        "Sugarcane": 2250,
        "Sunflower": 3700,
        "Urad": 4300,
        "Wheat": 1350
    }

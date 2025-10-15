# app/models/crop_data.py

commodity_dict = {
    "arhar": "app/static/Arhar.csv",
    "bajra": "app/static/Bajra.csv",
    "barley": "app/static/Barley.csv",
    "copra": "app/static/Copra.csv",
    "cotton": "app/static/Cotton.csv",
    "sesamum": "app/static/Sesamum.csv",
    "gram": "app/static/Gram.csv",
    "groundnut": "app/static/Groundnut.csv",
    "jowar": "app/static/Jowar.csv",
    "maize": "app/static/Maize.csv",
    "masoor": "app/static/Masoor.csv",
    "moong": "app/static/Moong.csv",
    "niger": "app/static/Niger.csv",
    "paddy": "app/static/Paddy.csv",
    "ragi": "app/static/Ragi.csv",
    "rape": "app/static/Rape.csv",
    "jute": "app/static/Jute.csv",
    "safflower": "app/static/Safflower.csv",
    "soyabean": "app/static/Soyabean.csv",
    "sugarcane": "app/static/Sugarcane.csv",
    "sunflower": "app/static/Sunflower.csv",
    "urad": "app/static/Urad.csv",
    "wheat": "app/static/Wheat.csv"
}

annual_rainfall = [29, 21, 37.5, 30.7, 52.6, 150, 299, 251.7, 179.2, 70.5, 39.8, 10.9]

base = {
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

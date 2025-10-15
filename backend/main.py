# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import forecast_routes

app = FastAPI(title="Crop Forecast API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(forecast_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Crop Forecast API"}

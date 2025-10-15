from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import forecast_routes

app = FastAPI(title="Crop Forecast API", version="1.0")

# CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routes
app.include_router(forecast_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Crop Forecast API!"}

@app.on_event("startup")
def startup_event():
    print("🚀 FastAPI server started successfully!")

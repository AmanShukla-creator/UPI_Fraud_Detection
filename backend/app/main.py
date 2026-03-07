from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database.models import Base
from app.database.db import engine
from app.routes.prediction import router as prediction_router
from app.routes.dashboard import router as dashboard_router
from app.routes.report import router as report_router
from app.routes.analytics import router as analytics_router
from app.routes.upi_risk import router as upi_risk_router
app = FastAPI(title="UPI Fraud Detection API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(dashboard_router)

app.include_router(prediction_router)

app.include_router(report_router)

app.include_router(upi_risk_router)

app.include_router(analytics_router)

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}
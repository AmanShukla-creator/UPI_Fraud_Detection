from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import Transaction

router = APIRouter()

@router.get("/dashboard/stats")
def get_dashboard_stats():

    db: Session = SessionLocal()

    total_transactions = db.query(Transaction).count()

    fraud_transactions = db.query(Transaction).filter(
        Transaction.prediction == "Fraud"
    ).count()

    fraud_rate = 0

    if total_transactions > 0:
        fraud_rate = (fraud_transactions / total_transactions) * 100

    db.close()

    return {
        "total_verifications": total_transactions,
        "fraud_detected": fraud_transactions,
        "fraud_rate": round(fraud_rate, 2)
    }
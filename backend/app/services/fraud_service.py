from app.database.db import SessionLocal
from app.database.models import Transaction

def predict_fraud(data):

    amount = data["amount"]

    if amount > 10000:
        prediction = "Fraud"
        probability = 0.85
    else:
        prediction = "Safe"
        probability = 0.15

    risk_score = int(probability * 100)

    db = SessionLocal()

    transaction = Transaction(
        amount=data["amount"],
        device_id=data["device_id"],
        location=data["location"],
        transaction_type=data["transaction_type"],
        prediction=prediction,
        risk_score=risk_score
    )

    db.add(transaction)
    db.commit()
    db.close()

    return {
        "prediction": prediction,
        "fraud_probability": probability,
        "risk_score": risk_score
    }
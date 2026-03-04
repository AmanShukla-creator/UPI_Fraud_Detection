from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    device_id = Column(String)
    location = Column(String)
    transaction_type = Column(String)
    prediction = Column(String)
    risk_score = Column(Integer)
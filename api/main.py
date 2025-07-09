from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from pymongo import MongoClient
import numpy as np
from datetime import datetime
import uuid

app = FastAPI()

# Load the model
model = load("model/fraud_model.joblib")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["fraud_detection"]
transactions = db["transactions"]

# Define the input data model
class Transaction(BaseModel):
    user_id: str
    amount: float
    location: str
    device_id: str

@app.post("/predict")
def predict(transaction: Transaction):
    # Prepare input for model
    features = np.array([[transaction.amount]])
    prediction = model.predict(features)[0]

    # Create full record to store
    transaction_record = transaction.dict()
    transaction_record["timestamp"] = datetime.utcnow()
    transaction_record["is_fraud"] = int(prediction)
    transaction_record["transaction_id"] = str(uuid.uuid4())

    # Save to MongoDB
    transactions.insert_one(transaction_record)

    return {
        "is_fraud": bool(prediction),
        "message": "Fraud detected!" if prediction else "Transaction is clean.",
        "saved": True
    }

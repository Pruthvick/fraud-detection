import random
import uuid
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["fraud_detection"]
transactions = db["transactions"]

users = [str(uuid.uuid4()) for _ in range(100)]
transactions.delete_many({})

for _ in range(5000):
    user_id = random.choice(users)
    amount = round(random.uniform(1.0, 1000.0), 2)

    is_fraud = int(
        (amount > 900 and random.random() > 0.3) or
        (random.random() < 0.015)
    )

    transaction = {
        "user_id": user_id,
        "amount": amount,
        "location": random.choice(["NY", "CA", "TX", "FL", "WA"]),
        "timestamp": datetime.utcnow() - timedelta(days=random.randint(0, 60)),
        "device_id": str(uuid.uuid4()),
        "is_fraud": is_fraud
    }

    transactions.insert_one(transaction)

print("✅ Inserted 5000 fake transactions into MongoDB.")

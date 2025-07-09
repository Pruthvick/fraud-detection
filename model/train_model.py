import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["fraud_detection"]
transactions = db["transactions"]

# Load data from MongoDB
df = pd.DataFrame(transactions.find())
print("Columns in DB:", df.columns.tolist())
print("First row:", df.head(1))


# Drop MongoDB's weird `_id` field
df = df.drop(columns=["_id"])

# Features and labels
X = df[["amount"]]  # for now we're only using amount
y = df["is_fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the model
dump(clf, "fraud_model.joblib")

print("Model trained and saved as 'fraud_model.joblib'.")

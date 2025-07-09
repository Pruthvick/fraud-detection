# fraud-detection

End-to-end fraud detection API powered by Python, MongoDB, and ML.

# Fraud Detection Pipeline 🚨

A full-stack project that simulates financial transactions, detects fraud using a machine learning model, and exposes predictions through a FastAPI backend.

## Stack
- Python
- Scikit-learn
- FastAPI
- MongoDB
- Uvicorn

## Features:
- Simulates 5,000+ realistic transaction records
- Stores and queries data using MongoDB
- Trains a machine learning model (RandomForest) to identify fraud patterns
- Provides a FastAPI-based REST endpoint for real-time fraud prediction
- Saves predictions back to the database for auditing and future retraining
  
## To Run:
- `simulate_transactions.py` to populate MongoDB
- `train_model.py` to train the model
- `uvicorn api.main:app --reload` to run the API

## Next Steps:
- Build Streamlit dashboard
- Add Docker support
- Deploy API


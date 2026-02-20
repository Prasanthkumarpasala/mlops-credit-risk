import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

print("Loading Production model from MLflow Registry...")

model = mlflow.pyfunc.load_model(
    model_uri="./mlruns/1/models/m-6ac642dd1e7a4b99a4254b744a90e964/artifacts"
)

print("Model loaded successfully!")


# ✅ Input schema
class CreditInput(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: int
    employment_years: int
    previous_defaults: int
    debt_to_income_ratio: float


# ✅ Home endpoint
@app.get("/")
def home():
    return {"message": "Credit Risk API is running!"}


# ✅ Prediction endpoint
@app.post("/predict")
def predict(data: CreditInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)
    return {"prediction": int(prediction[0])}
import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "age": np.random.randint(21, 60, n),
    "income": np.random.randint(20000, 150000, n),
    "loan_amount": np.random.randint(5000, 50000, n),
    "credit_score": np.random.randint(300, 850, n),
    "employment_years": np.random.randint(0, 20, n),
    "previous_defaults": np.random.randint(0, 3, n),
})

data["debt_to_income_ratio"] = data["loan_amount"] / data["income"]

# Create target logically
data["loan_approved"] = (
    (data["credit_score"] > 600) &
    (data["debt_to_income_ratio"] < 0.4) &
    (data["previous_defaults"] == 0)
).astype(int)

data.to_csv("data/raw/credit_data.csv", index=False)

print("Dataset created successfully")
print(data.head())
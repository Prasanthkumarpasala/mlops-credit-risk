import os
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from data_loader import load_data

DATA_PATH = "data/raw/credit_data.csv"
MODEL_PATH = "models/model.pkl"

def train():

    mlflow.set_experiment("Credit_Risk_Experiment")

    with mlflow.start_run():

        print("Loading dataset...")
        data = load_data(DATA_PATH)

        X = data.drop("loan_approved", axis=1)
        y = data["loan_approved"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        n_estimators = 200

        model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=42
        )

        print("Training model...")
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        print(f"Accuracy: {accuracy:.4f}")

        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)

        # Save model locally
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        # Log model to MLflow
        mlflow.sklearn.log_model(model,artifact_path="model",registered_model_name="CreditRiskModel")

        print("Model logged to MLflow successfully!")

if __name__ == "__main__":
    train()
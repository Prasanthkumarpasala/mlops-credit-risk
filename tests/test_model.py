import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import load_data

def test_data_loading():
    data = load_data("data/raw/credit_data.csv")
    assert data.shape[0] > 0
    assert "loan_approved" in data.columns
    
import pandas as pd
from src.data_loader import load_data

def test_data_loading(tmp_path):
    # Create dummy CSV
    dummy_file = tmp_path / "dummy.csv"
    
    df = pd.DataFrame({
        "feature1": [1, 2, 3],
        "loan_approved": [0, 1, 0]
    })
    
    df.to_csv(dummy_file, index=False)

    data = load_data(dummy_file)

    assert data.shape[0] == 3
    assert "loan_approved" in data.columns
    
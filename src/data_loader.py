import pandas as pd

def load_data(path: str):
    """
    Load dataset from given path
    """
    data = pd.read_csv(path)
    return data
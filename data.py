# data.py
import pandas as pd
def read_data(url):
    """
    Reads data from a URL using pandas and returns a pandas DataFrame.
    """
    data = pd.read_csv(url)
    return data
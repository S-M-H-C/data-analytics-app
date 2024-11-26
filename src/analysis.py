import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('data/sample_data.csv')

    # Perform analysis (e.g., calculate mean)
    mean_value = data['Humidity'].mean()

    return {'mean': mean_value}

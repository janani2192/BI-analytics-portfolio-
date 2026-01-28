import pandas as pd

# Load raw transaction data
transactions = pd.read_csv("../data/raw_transactions.csv")

# Inspect
print(transactions.head())
print(transactions.info())

import pandas as pd
import numpy as np

np.random.seed(7)

n_rows = 1200

stages = ["Prospecting", "Qualified", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]
regions = ["NA", "EMEA", "APAC", "LATAM"]
products = ["Core Payments", "Risk Solutions", "VAS", "Analytics"]

df = pd.DataFrame({
    "opportunity_id": range(1, n_rows + 1),
    "deal_amount": np.round(np.random.lognormal(mean=10, sigma=0.6, size=n_rows), 2),
    "discount_pct": np.round(np.random.normal(12, 5, n_rows), 1),
    "stage": np.random.choice(stages, n_rows),
    "days_in_stage": np.random.randint(3, 120, n_rows),
    "region": np.random.choice(regions, n_rows),
    "product": np.random.choice(products, n_rows),
    "probability": np.round(np.random.uniform(0.2, 0.95, n_rows), 2),
})

df["expected_revenue"] = df["deal_amount"] * df["probability"]

df.to_csv("../data/raw_opportunities.csv", index=False)

print("raw_opportunities.csv created.")

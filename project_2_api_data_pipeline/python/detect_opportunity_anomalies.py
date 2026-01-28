import pandas as pd
from sklearn.ensemble import IsolationForest

# -----------------------
# Load data
# -----------------------

df = pd.read_csv("../data/raw_opportunities.csv")

# -----------------------
# Prepare features
# -----------------------

features = ["deal_amount", "discount_pct", "days_in_stage", "probability"]

X = df[features]

# -----------------------
# Train anomaly model
# -----------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.03,
    random_state=42
)

df["anomaly_score"] = model.fit_predict(X)
df["is_anomaly"] = df["anomaly_score"] == -1


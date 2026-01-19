import requests
import pandas as pd

# API endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

# API request
response = requests.get(url, params=params)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    # Convert JSON to DataFrame
    df = pd.DataFrame(data)

    # Select relevant columns
    df = df[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h"
        ]
    ]

    # Save to data folder
    df.to_csv("../data/crypto_market_data.csv", index=False)

    print("Data successfully extracted and saved.")
else:
    print("API request failed:", response.text)

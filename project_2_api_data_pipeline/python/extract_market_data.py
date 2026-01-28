import requests
import pandas as pd
import time

URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1
}

all_data = []

while True:
    print(f"Fetching page {PARAMS['page']}")

    response = requests.get(URL, params=PARAMS)

    if response.status_code != 200:
        print(f"Request failed with status {response.status_code}")
        break

    page_data = response.json()

    if not page_data:
        print("No more data. Stopping pagination.")
        break

    all_data.extend(page_data)
    PARAMS["page"] += 1

    time.sleep(1)

df = pd.DataFrame(all_data)

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

df.to_csv("../data/crypto_market_data_paginated.csv", index=False)

print("Paginated data extraction completed successfully.")

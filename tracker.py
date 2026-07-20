import requests
import pandas as pd
import time
import os
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
FILE_NAME = "btc_price_history.csv"

def fetch_price():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        return {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "price": data['bitcoin']['eur']}
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_and_display():
    # Read the CSV to calculate insights
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        # Calculate moving average of the last 5 entries
        avg_price = df['price'].tail(5).mean()
        print(f"--- Insights: Average of last 5 entries: €{avg_price:.2f} ---")

print("Starting Pipeline with Transformation...")
try:
    while True:
        data_point = fetch_price()
        if data_point:
            # Save
            df = pd.DataFrame([data_point])
            df.to_csv(FILE_NAME, mode='a', index=False, header=not os.path.exists(FILE_NAME))
            
            # Display & Transform
            print(f"[{data_point['timestamp']}] Saved: €{data_point['price']}")
            process_and_display()
            
        time.sleep(10)
except KeyboardInterrupt:
    print("\nPipeline finished.")
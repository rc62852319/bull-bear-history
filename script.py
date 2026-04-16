import requests
import json
from datetime import datetime, timedelta

url = "https://www.warrants.hsbc.com.hk/tc/cbbc/cbbcBandChart?pricedetails=1&ucode=HSI&step=10&spread=100"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
data = response.json()

rows = []

# Extract CBBC outstanding rows
for item in data.get("mainData", []):
    price_range = item.get("range", "")
    bull = item.get("bullvalue", "")
    bear = item.get("bearvalue", "")
    rows.append([price_range, bull, bear])

# Extract previous close
further = data.get("furtherData", {})
last_close = (
    further.get("pclose")
    or further.get("lastclose")
    or further.get("last")
    or "N/A"
)

rows.append(["上日收市價", last_close, ""])

# Use Hong Kong date
hk_time = datetime.utcnow() + timedelta(hours=8)
today = hk_time.strftime("%Y-%m-%d")

with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

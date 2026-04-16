import requests
import json
from datetime import datetime, timedelta

url = "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI?format=json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI",
    "X-Requested-With": "XMLHttpRequest"
}

response = requests.get(url, headers=headers)
data = response.json()

rows = []

# Extract CBBC rows
for item in data["data"]:
    rows.append([item["range"], item["outstanding"]])

# Add previous close
rows.append(["上日收市價", data["last_close"]])

# Use Hong Kong date
hk_time = datetime.utcnow() + timedelta(hours=8)
today = hk_time.strftime("%Y-%m-%d")

with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

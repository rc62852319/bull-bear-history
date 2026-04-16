import requests
import json
from datetime import datetime, timedelta

url = "https://www.warrants.hsbc.com.hk/tc/data/chart/cbbcBandChart?pricedetails=1&ucode=HSI&step=10&spread=100&sdate="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
data = response.json()

rows = []

# mainData holds the CBBC bands
main_data = data.get("mainData", [])

for item in main_data:
    # Try a few likely key names to be robust
    price_range = item.get("band") or item.get("range") or item.get("price") or ""
    bull = item.get("bull") or item.get("bullvalue") or item.get("bull_oi") or ""
    bear = item.get("bear") or item.get("bearvalue") or item.get("bear_oi") or ""
    rows.append([price_range, bull, bear])

# furtherData may contain previous close
further = data.get("furtherData", {}) or {}
last_close = (
    further.get("pclose")
    or further.get("lastclose")
    or further.get("last_close")
    or "N/A"
)

rows.append(["上日收市價", last_close, ""])

# Use Hong Kong date
hk_time = datetime.utcnow() + timedelta(hours=8)
today = hk_time.strftime("%Y-%m-%d")

with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

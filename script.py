import requests
import json
from datetime import datetime

url = "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI?format=json"
data = requests.get(url).json()

rows = []

# The CBBC table is inside data["data"]
for item in data["data"]:
    rows.append([item["range"], item["outstanding"]])

# Add previous close at the bottom
rows.append(["上日收市價", data["last_close"]])

today = datetime.now().strftime("%Y-%m-%d")
with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

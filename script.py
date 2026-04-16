import requests
import json
from datetime import datetime

url = "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI"

r = requests.get(url)
html = r.text

# ⚠️ IMPORTANT:
# You will likely need to inspect HTML to extract real values

# placeholder example:
data = []

try:
    with open("data/hsidata.json", "r") as f:
        data = json.load(f)
except:
    data = []

data.append({
    "date": datetime.now().strftime("%Y-%m-%d"),
    "value": "PLACEHOLDER"
})

with open("data/hsidata.json", "w") as f:
    json.dump(data, f, indent=2)

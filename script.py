import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"class": "table table-striped table-hover"})
rows = []

for tr in table.find_all("tr"):
    cols = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
    if cols:
        rows.append(cols)

today = datetime.now().strftime("%Y-%m-%d")
with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

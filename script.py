import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

# The CBBC table is the SECOND table on the page
tables = soup.find_all("table")
table = tables[1]  # index 1 = second table

rows = []

for tr in table.find_all("tr"):
    cols = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
    if len(cols) == 2:  # only keep rows with 2 columns
        rows.append(cols)

# Extract previous close from the page
last_close = soup.find("span", {"id": "lastClose"}).get_text(strip=True)
rows.append(["上日收市價", last_close])

today = datetime.now().strftime("%Y-%m-%d")
with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

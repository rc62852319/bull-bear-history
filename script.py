import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.jpmhkwarrants.com/zh_hk/cbbc/cbbc-outstanding/HSI"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

html = requests.get(url, headers=headers).text
print(html)
soup = BeautifulSoup(html, "html.parser")

# The CBBC table is the second table on the page
tables = soup.find_all("table")
table = tables[1]

rows = []

for tr in table.find_all("tr"):
    cols = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
    if len(cols) == 2:
        rows.append(cols)

# The last row already contains 上日收市價
# No need to extract lastClose separately

today = datetime.now().strftime("%Y-%m-%d")
with open(f"data/{today}.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

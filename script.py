import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

url = "https://www.warrants.hsbc.com.hk/tc/cbbc/cbbc-map/type/outstanding"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

rows = []

# Find the CBBC outstanding table
table = soup.find("table")

# Extract table rows
for tr in table.find_all("tr"):
    cols = [td.get_text(strip=True) for td in tr.find_all("td")]
    if len(cols) == 3:
        price_range = cols[0]
        bull = cols[1]
        bear = cols[2]
        rows.append([price_range, bull, bear])

# Extract previous close (上日收市價)
last_close_el = soup.find("span", {"class": "last-close"})
if last_close_el:
    last_close = last_close_el.get_text(strip=True)
    rows.append(["上日收市價", last_close, ""])
else:
    rows.append(["上日收市價", "N/A", ""])


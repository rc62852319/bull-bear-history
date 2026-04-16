import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

url = "https://www.warrants.hsbc.com.hk/tc/cbbc/cbbc-map/type/outstanding"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

# Fetch HTML
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

rows = []

# Find the CBBC outstanding table (first table on the page)
table = soup.find("table")

# Extract table rows (price range, bull, bear)
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

# -----------------------------
# ⭐ DATE + SAVE SECTION
# -----------------------------

# Use Hong Kong date
hk_time = datetime.utcnow() + timedelta(hours=8)

# TEMPORARY OVERRIDE FOR TESTING
today = "2026-04-17"   # ← Force new file for testing

# Normally you would use:
# today = hk_time.strftime("%Y-%m-%d")

# Save JSON file
with open(f"data/{today}.json

import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://azure.microsoft.com/en-us/pricing/details/app-service/linux/"
PLANS = ["P1v3", "P2v3", "P3v3"]
REGION = "europe-west"
FILE = "appservice_prices.json"

# Load previous prices if available
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        saved_prices = json.load(f)
else:
    saved_prices = {}

current_prices = {}

# Scrape latest prices
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

for plan in PLANS:
    td = soup.find("td", string=lambda s: s and plan in s)
    if not td:
        continue

    one_year_td = td.find_next("td", class_="discounted-price")
    if not one_year_td:
        continue

    price_span = one_year_td.find("span", class_="price-data")
    if not price_span:
        continue

    try:
        data_json = json.loads(price_span["data-amount"])
        price = data_json["regional"].get(REGION)
        if price:
            rounded_price = round(float(price), 3)
            current_prices[plan] = rounded_price
    except Exception as e:
        print(f"Error parsing {plan}: {e}")

# Compare and print changes
for plan, price in current_prices.items():
    old_price = saved_prices.get(plan)
    if old_price is None:
        print(f"{plan}: initial price ${price:.3f}/hour")
    elif old_price != price:
        print(f"⚠️ {plan} price changed: was ${old_price:.3f}, now ${price:.3f}")
    else:
        print(f"{plan}: no change (${price:.3f}/hour)")

# Save current prices
with open(FILE, "w") as f:
    json.dump(current_prices, f, indent=2)

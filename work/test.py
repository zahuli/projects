import requests
from bs4 import BeautifulSoup
import json

URL = "https://azure.microsoft.com/en-us/pricing/details/app-service/linux/"
PLANS = ["P1v3", "P2v3", "P3v3"]
REGION = "europe-west"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

for plan in PLANS:
    # find the table cell with the plan name (e.g. P1v3)
    td = soup.find("td", string=lambda s: s and plan in s)
    if not td:
        print(f"{plan}: not found")
        continue

    # move two <td> forward: one is pay-as-you-go, next is 1-year-savings
    one_year_td = td.find_next("td", class_="discounted-price")
    if not one_year_td:
        print(f"{plan}: 1-year savings cell not found")
        continue

    price_span = one_year_td.find("span", class_="price-data")
    if not price_span:
        print(f"{plan}: price data not found")
        continue

    try:
        data_json = json.loads(price_span["data-amount"])
        price = data_json["regional"].get(REGION)
        if price is None:
            print(f"{plan}: region '{REGION}' not found")
            continue

        rounded_price = round(float(price), 3)
        print(f"{plan}: ${rounded_price:.3f}/hour")

    except Exception as e:
        print(f"{plan}: error parsing data - {e}")

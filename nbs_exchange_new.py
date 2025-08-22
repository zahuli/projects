import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_exchange_rate(currency: str, date: str) -> float:
    """
    Fetch exchange rate for a given currency and date
    from NBS website.
    """

    # Validate and format date
    try:
        date_obj = datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        raise ValueError(
            "❌ Date must be in format dd.mm.yyyy (e.g., 06.08.2025)")

    if date_obj.date() > datetime.today().date():
        raise ValueError("❌ Date cannot be in the future")

    # Construct URL
    url = (
        f"https://webappcenter.nbs.rs/ExchangeRateWebApp/ExchangeRate/IndexByDate"
        f"?isSearchExecuted=true&Date={date}&ExchangeRateListTypeID=3"
    )

    # Fetch page
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(
            f"❌ Failed to fetch data from NBS (status {response.status_code})")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "table"})

    if not table:
        raise Exception("❌ Exchange rate table not found on page")

    # Extract rows
    for row in table.find_all("tr"):      # Iterate through each table row
        cols = [c.get_text(strip=True)
                for c in row.find_all("td")]   # Collect cell texts
        # First column is the currency code (e.g., 'USD')
        if cols and cols[0] == currency:
            # Last column is the rate
            rate_str = cols[-1].replace(",", ".")  # Replace comma with dot
            return float(rate_str)

    raise ValueError(f"❌ Currency {currency} not found in table")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 nbs_exchange_new.py <dd.mm.yyyy> <USD_amount>")
        sys.exit(1)

    date = sys.argv[1]
    usd_amount = float(sys.argv[2])

    eur_rate = get_exchange_rate("EUR", date)
    usd_rate = get_exchange_rate("USD", date)

    eur_value = round(((usd_rate * usd_amount) / eur_rate), 2)

    print(f"Na dan {date} kurs evra je {eur_rate}, kurs dolara je {usd_rate}")
    print(f"{usd_amount} USD je konvertovano {eur_value} EUR")

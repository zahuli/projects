# https://www.nbs.rs/kursnaListaModul/naZeljeniDan.faces
# python3 nbs_kurs.py 04/05/2023 1000

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys


def get_exchange_rate(currency: str, date: str) -> float:
    # Create a new instance of the Chrome driver
    try:
        driver = webdriver.Chrome()
    except Exception as e:
        driver = webdriver.Firefox()
    # Navigate to the web page with the date input field and currency input field
    driver.get("https://www.nbs.rs/kursnaListaModul/naZeljeniDan.faces")

    # Find the date input field and enter the desired date
    date_input = driver.find_element(By.ID, 'index:inputCalendar1')

    date_input.clear()
    date_input.send_keys(date)

    # identify dropdown with Select class
    type_rate = Select(driver.find_element(
        By.XPATH, '//*[@id="index:vrstaInner"]'))
    # select by select_by_visible_text() method
    type_rate.select_by_visible_text("Middle Exchange Rate")

    driver.find_element(By.XPATH, '//*[@id="index:buttonShow"]').click()

    # dodati citanje tabele
    table_id = driver.find_element(By.ID, 'index:srednjiKursLista')
    # get all of the rows in the table
    rows = table_id.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        s = str(row.text).split()
        if s[0] == currency:
            return float(s[-1])

    driver.quit()


# date = "27/04/2023"
# usd = 1100

date = str(sys.argv[1])
usd = int(sys.argv[2])


eur_rate = get_exchange_rate("EUR", date)
usd_rate = get_exchange_rate("USD", date)

eur = round(((usd_rate * usd) / eur_rate), 2)


print(f"Na dan {date} kurs evra je {eur_rate}, kurs dolara je {usd_rate}")
print(f"{usd} je konvertovano {eur}")

import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
response = requests.get(os.environ["URL"], headers={
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15"
})

data = response.text
soup = BeautifulSoup(data, "html.parser")

price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("€")[1]
price_as_float = float(price_without_currency)

msg = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 130

if price_as_float < BUY_PRICE:
    message = f"{msg}is now ${price_as_float}"
    with smtplib.SMTP(host=os.environ["host"]) as connection:
        connection.starttls()
        connection.login(os.environ["From"], os.environ["Password"])
        connection.sendmail(
            from_addr=os.environ["From"],
            to_addrs=os.environ["To"],
            msg=f"Subject:Amazon Price Alert\n\n{message}\n{os.environ["URL"]}".encode(),
        )



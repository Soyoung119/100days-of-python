import requests
from datetime import datetime, timedelta
import yfinance as yf
import json
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_PHONE_NUMBER = "sender_phone_number"
MY_PHONE_NUMBER = "your_phone_number"

news_url = "https://newsapi.org/v2/everything"
new_params = {
    "apiKey": "your_apiKey",
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
}

account_sid= "your_account_sid"
auth_token= "your_token"

now_date = datetime.now()
start_date = now_date - timedelta(days=2)

finance = yf.download("TSLA", start=start_date)

data = finance.reset_index().to_json(
    orient="records",
    date_format="iso"
)

records = json.loads(data)
# print(records)
# url = "https://www.alphavantage.co/query"
#
# params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "interval": "60min",
#     "apikey": "KZ128C2C4J6FBC1D"
#         }
#
# response = requests.get(url, params=params)
# data = response.json()
# data

close_list = []
data_date = records[:2]
for close in data_date:
    close_amount = close["('Close', 'TSLA')"]
    close_list.append(close_amount)

percentage = (close_list[1] - close_list[0]) / close_list[0] * 100

response = requests.get(news_url, params=new_params)
response.raise_for_status()
news_data = response.json()

article_list = []
news_data = news_data["articles"][:3]

for title in news_data:
    headlines = title["title"]
    description = title["description"]
    article_list.append({"headlines": headlines, "description": description})

# message_up = f"{STOCK}: 🔺{percentage}%\n"
# for n in range(3):
#         message_up += (
#             f"Headlines: {article_list[n]["headlines"]}\n"
#             f"Brief: {article_list[n]["description"]}\n\n"
#         )
#
# message_down = f"{STOCK}: 🔻{percentage}%\n"
# for n in range(3):
#         message_up += (
#             f"Headlines: {article_list[n]["headlines"]}\n"
#             f"Brief: {article_list[n]["description"]}\n\n"
#         )
#
# # if percentage > 0:
# if percentage > 5:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         to=MY_PHONE_NUMBER,
#         from_=TWILIO_PHONE_NUMBER,
#         body="sms_appointment_reminders",
#         # body=message_up
#     )
#     print(message.status)
#
# # elif percentage < 0:
# elif percentage < -5:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         to=MY_PHONE_NUMBER,
#         from_=TWILIO_PHONE_NUMBER,
#         body="sms_appointment_reminders",
#         # body=message_down
#     )
#     print(message.status)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


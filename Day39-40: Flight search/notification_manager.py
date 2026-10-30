import requests
import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self, price, destination, cheapest_date):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            to=os.environ["To_number"],
            from_=os.environ["From_number"],
            # body=f"Low price alert! Only €{price} to fly from LON to {destination}, on {cheapest_date}",
            body="sms_appointment_reminders",
        )
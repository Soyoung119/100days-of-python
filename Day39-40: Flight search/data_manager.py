import requests
import os
from dotenv import load_dotenv
from pprint import pprint

class DataManager:
    def __init__(self):
        load_dotenv()
        self.sheet_endpoint = os.getenv("Sheety_endpoint")
        self.headers = {
            "Authorization": os.getenv("Authorization"),
        }

    def import_data(self):
        self.response = requests.get(url=self.sheet_endpoint, headers=self.headers)
        self.sheet_data = self.response.json()["prices"]
        pprint(self.sheet_data)

    def update(self, object_id, code, price):
        self.update_endpoint = f"{self.sheet_endpoint}/{object_id}"

        self.update_data = {
            "price": {
                "iataCode": code,
                "lowestPrice": price
            }
        }

        self.response1 = requests.put(url=self.update_endpoint, headers=self.headers, json=self.update_data)
        self.data1 = self.response1.json()
        print(self.response1.text)


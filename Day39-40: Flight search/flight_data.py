import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

MY_LOCATION = "LON"

# load_dotenv()
# tomorrow = datetime.now() + timedelta(days=1)
# end_date = tomorrow + timedelta(days=7)
#
# flight_endpoint = "https://api.duffel.com/air/offer_requests"
# flight_headers = {
#             "Authorization": f"Bearer {os.getenv("TOKEN")}",
#             "Duffel-Version": "v2",
#             "Accept-Encoding": "gzip",
#             "Accept": "application/json",
#             "Content-Type": "application/json"
#         }
#
# prices = []
# while tomorrow <= end_date:
#     flight_data = {
#         "data": {
#             "slices": [
#                 {
#                     "origin": MY_LOCATION,
#                     "destination": "ICN",
#                     "departure_date": tomorrow.strftime("%Y-%m-%d")
#                 }
#             ],
#             "passengers": [
#                 {
#                     "type": "adult"
#                 }
#             ],
#             "cabin_class": "economy"
#         }
#     }
#     flight_response = requests.post(url=flight_endpoint, json=flight_data,
#                                     headers=flight_headers)
#     print(flight_response.json())
#     flight_offer = flight_response.json()["data"]["offers"]
#     try:
#         price = min(float(offer["total_amount"]) for offer in flight_offer)
#         print(price)
#         prices.append(price)
#     except ValueError:
#         print("No flight offer")
#
#     tomorrow += timedelta(days=1)
#
# cheapest_price = min(prices)
# print(cheapest_price)


class FlightData:
    def __init__(self):
        load_dotenv()
        self.flight_endpoint = "https://api.duffel.com/air/offer_requests"
        self.flight_headers = {
            "Authorization": f"Bearer {os.getenv("TOKEN")}",
            "Duffel-Version": "v2",
            "Accept-Encoding": "gzip",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def find_cheapest_flight(self, destination):
        self.prices = []

        self.tomorrow = datetime.now() + timedelta(days=1)
        self.end_date = self.tomorrow + timedelta(days=4)

        while self.tomorrow <= self.end_date:
            self.flight_data = {
                "data": {
                    "slices": [
                        {
                            "origin": MY_LOCATION,
                            "destination": destination,
                            "departure_date": self.tomorrow.strftime("%Y-%m-%d")
                        }
                    ],
                    "passengers": [
                        {
                            "type": "adult"
                        }
                    ],
                    "cabin_class": "economy"
                }
            }
            flight_response = requests.post(url=self.flight_endpoint, json=self.flight_data,
                                            headers=self.flight_headers)

            response_data = flight_response.json()

            if "data" in response_data and "offers" in response_data["data"]:
                flight_offer = response_data["data"]["offers"]

                try:
                    price = min(float(offer["total_amount"]) for offer in flight_offer)
                    self.prices.append({
                        "price": price,
                        "date": self.tomorrow.strftime("%Y-%m-%d")
                    })

                except ValueError:
                    print("No flight offer")

            else:
                print("NO DATA/OFFERS")
                print(response_data)

            self.tomorrow += timedelta(days=1)

        if self.prices:
            cheapest_flight = self.prices[0]

            for flight in self.prices:
                if flight["price"] < cheapest_flight["price"]:
                    cheapest_flight = flight

            return cheapest_flight["price"], cheapest_flight["date"]

        else:
            print("No prices found")
            return None


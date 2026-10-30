import requests
import os
from dotenv import load_dotenv



# iata_endpoint = "https://airportsapi.com/api/airports"
# iata_headers = {
#     "Accept": "application/json"
# }
# iata_params = {
#     "filter[name]": "Dublin"
# }
# response = requests.get(url=iata_endpoint, headers=iata_headers, params=iata_params)
# response.raise_for_status()
# data = response.json()["data"][0:]
# iata_code = [airport["attributes"]["iata_code"] for airport in data
#              if airport["attributes"]["iata_code"] is not None]
# print(iata_code)

# load_dotenv()
# flight_endpoint = "https://api.duffel.com/air/offer_requests"
#
# flight_headers = {
#     "Authorization": f"Bearer {os.getenv("TOKEN")}",
#     "Duffel-Version": "v2",
#     "Accept-Encoding": "gzip",
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }
#
# flight_data = {
#     "data":{
#         "slices":[
#             {
#                 "origin": MY_LOCATION,
#                 "destination": "ICN",
#                 "departure_date": "2026-08-10"
#             }
#         ],
#         "passengers":[
#             {
#                 "type": "adult"
#             }
#         ],
#         "cabin_class": "economy"
#     }
# }
#
# response = requests.post(url=flight_endpoint, json=flight_data, headers=flight_headers)
# data = response.json()["data"]["offers"]
# result=min(float(offer["total_amount"]) for offer in data)
# print(result)

class FlightSearch:
    def __init__(self):
        self.iata_endpoint = "https://airportsapi.com/api/airports"
        self.iata_headers = {
            "Accept": "application/json"
        }

    def search_iata(self, city):
        self.iata_params = {
            "filter[name]": city
        }
        response = requests.get(url=self.iata_endpoint, headers=self.iata_headers, params=self.iata_params)
        response.raise_for_status()
        data = response.json()["data"][0:]
        self.iata_code = [airport["attributes"]["iata_code"] for airport in data
                     if airport["attributes"]["iata_code"] is not None]
        self.iata_code = ", ".join(self.iata_code)
        return self.iata_code
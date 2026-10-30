from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()



data_manager.import_data()
data_slice = data_manager.sheet_data

# for iata in data_slice:
#     iata_code = iata["iataCode"]
#     iata_city = iata["city"]
#     if iata_code == "":
#         iata["iataCode"] = flight_search.search_iata(iata_city)
#         data_manager.update(iata["id"], flight_search.iata_code)

for iata in data_slice:
    iata_code = iata.get("iataCode")
    iata_city = iata["city"]
    iata_lowest_price = iata["lowestPrice"]

    if not iata_code:
        iata_code = flight_search.search_iata(iata_city)
        data_manager.update(iata["id"], iata_code, iata_lowest_price)

    prices = []

    for code in iata_code.split(", "):
        print("SEARCHING:", code)

        result = flight_data.find_cheapest_flight(code)

        if result[0] is not None:
            price = result[0]
            date = result[1]

            print("RESULT:", price, date)

            prices.append({
                "price": price,
                "date": date,
                "code": code
            })

    if prices:
        cheapest_flight = prices[0]

        for flight in prices:
            if flight["price"] < cheapest_flight["price"]:
                cheapest_flight = flight

        cheapest_price = cheapest_flight["price"]
        cheapest_date = cheapest_flight["date"]
        cheapest_code = cheapest_flight["code"]

        print("CHEAPEST:", cheapest_price)
        print("DATE:", cheapest_date)

        if iata_lowest_price > cheapest_price:
            data_manager.update(
                iata["id"],
                iata_code,
                cheapest_price
            )

            NotificationManager(
                cheapest_price,
                cheapest_code,
                cheapest_date
            )

    else:
        print(f"No prices found for {iata_city}")






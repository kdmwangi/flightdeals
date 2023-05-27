import requests
from datetime import datetime
from pprint import pprint
from data_manager import DataManager
class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def searching_flights(self):

        SHEETS_ENDPOINT = "https://api.sheety.co/0787d74e4153aa2868fb41900212715e/flightDeals/prices"
        SHEETY_UPDATE_ENDPOINT = "https://api.sheety.co/c9c4b407ab43ef84bc6a79436df14325/flightDeals/prices/10"
        FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        SHEETY_HEADERS = {

        }
        TEQUILA_KEY = "0vsWVLna1emSIMW76eKLvCvgT6WNeR7h"
        TEQUILA_APPID = "kdennisflightsearch"

        flight_search_data = []
        # flight_info = to_visit
        future_six_months = datetime.today()
        future_month = ((future_six_months.month + 6) % 12)
        future_date = future_six_months.day
        future_year = round((future_six_months.year + (future_six_months.month + 6) / 12))
        six_months_time = f"{future_date}/{future_month}/{future_year}"

        today = datetime.now()
        td = today.strftime("%d/%m/%Y")
        # for destination in flight_info:

            # print(destination['iataCode'])

        flight_data = {
            "adults": 1,
            "fly_from": "LON",
            "fly_to": 'PAR',
            "date_from ": td,
            "date_to ": six_months_time,
            "curr": "GBP",
            "one_for_city":1,
            "flight_type":"round",
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 28,
            "price_to": 54,
            "max_stopovers":0,

        }

        headers = {
            "apikey": TEQUILA_KEY
        }
        response2 = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_data, headers=headers)
        response2.raise_for_status()

        flight_search_data.append(response2.json()['data'])
        if not flight_search_data[0]:
            ...
        else:

            pprint(flight_search_data)
        return flight_search_data


fl = FlightSearch()
fl.searching_flights()
# endpoint = "https://tequila-api.kiwi.com/locations/query"
# headers = {
#     "apikey":"0vsWVLna1emSIMW76eKLvCvgT6WNeR7h"
#
# }

# params = {
#     "term":"Nairobi",
# }
#
# response = requests.get(url=endpoint, params=params, headers=headers)
# response.raise_for_status()
# print(response.json()['locations'][0]['code'])
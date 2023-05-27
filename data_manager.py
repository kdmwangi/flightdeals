class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def sheets_data(self):
        from requests.auth import HTTPBasicAuth
        import requests
        from datetime import datetime
        from twilio.rest import Client
        SHEETS_ENDPOINT = "https://api.sheety.co/0787d74e4153aa2868fb41900212715e/flightDeals/prices"
        SHEETY_UPDATE_ENDPOINT = "https://api.sheety.co/c9c4b407ab43ef84bc6a79436df14325/flightDeals/prices/10"
        FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        SHEETY_HEADERS = {

        }
        TEQUILA_KEY = "0vsWVLna1emSIMW76eKLvCvgT6WNeR7h"
        TEQUILA_APPID = "kdennisflightsearch"

        today = datetime.now()
        td = today.strftime("%d/%m/%Y")
        response = requests.get(url=SHEETS_ENDPOINT, auth=HTTPBasicAuth('mwangi', 'bnVsbDpudWxs'))
        response.raise_for_status()
        # print(response.status_code)
        SHEETS_CITIES = response.json()['prices']
        # use list comprehension
        flight_info = [item for item in SHEETS_CITIES]
        return  flight_info
# data = {
#     "price":{
#         'iataCode': 'CPT',
#     }
# }
# update the city with the IATA codes
# response1 = requests.put(url=SHEETY_UPDATE_ENDPOINT, auth=HTTPBasicAuth('mwangi', 'bnVsbDpudWxs'), json=data)
# response1.raise_for_status()
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#this contains the procedural approach of the flight deals capstone project
from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
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
# print(flight_info)
# use dictionary comprehension on the list

#search of city code via flight api
# *****************************************************************************************
endpoint = "https://tequila-api.kiwi.com/locations/query"
headers = {
    "apikey":"0vsWVLna1emSIMW76eKLvCvgT6WNeR7h"

}

params = {
    "term":"Nairobi",
}

response = requests.get(url=endpoint, params=params, headers=headers)
response.raise_for_status()
# print(response.json()['locations'][0]['code'])
# ***************************************************************************************
data = {
    "price":{
        'iataCode': 'CPT',
    }
}
# update the city with the IATA codes
# response1 = requests.put(url=SHEETY_UPDATE_ENDPOINT, auth=HTTPBasicAuth('mwangi', 'bnVsbDpudWxs'), json=data)
# response1.raise_for_status()

future_six_months = datetime.today()
future_month = ((future_six_months.month+6)%12)
future_date = future_six_months.day
future_year = round((future_six_months.year + (future_six_months.month+6) /12))
six_months_time = f"{future_date}/{future_month}/{future_year}"
# print(six_months_time)

flight_search_data = []
for destination in flight_info:
    # print(destination['iataCode'])

    flight_data = {
        "adults":1,
        "fly_from":"LON",
        "fly_to": destination['iataCode'],
        "date_from ":td,
        "date_to ": six_months_time,
        "curr": "GBP",
        "one_for_city":1,
        # "price_to":destination['lowestPrice'],
        "max_stopovers":0,
        # "flight_type": "round",



    }

    headers = {
        "apikey":TEQUILA_KEY
    }
    response2 = requests.get(url=FLIGHT_SEARCH_ENDPOINT,  params=flight_data, headers=headers)
    response2.raise_for_status()
    flight_search_data.append(response2.json()['data'])

# print(flight_search_data[0])
search_price_result = []
for flight in flight_search_data[:10]:
    if flight:
        search_price_result.append(flight)

# print(search_price_result)
# send an sms with all the flights that are lower than our defined lowest price in our google sheets
# departure airport iata code ['flyFrom]
# destination airport iata code ['flyTo']
# departure city ['cityForm']
# destination city ['cityTo']
# flight price ['price']
# and flight dates ['local_arrival'] ['local_departure]



for x in search_price_result:

    # print(x)
    for m in range(len(x)):
        print(x[m]['flyFrom'])
        from_code = x[m]['flyFrom']

        print(x[m]['flyTo'])
        to_code=x[m]['flyTo']

        print(x[m]['cityFrom'])
        from_city = x[m]['cityFrom']

        print(x[m]['cityTo'])
        to_city =x[m]['cityTo']

        a_t = x[m]['local_arrival'].split('T')
        print(a_t[0])
        d_t = x[m]['local_departure'].split('T')
        print(d_t[0])
        price = x[m]['price']
        print(f"${x[m]['price']}")


        account_sid = "ACf52a092602490fcd210e96d7190fe39d"
        auth_token = "fab84f7d55d29edbc0a00a851750bfd1"
        client = Client(account_sid, auth_token)
        for destination in flight_info:
            if(x[m]["price"] < destination['lowestPrice']):
                message = client.messages \
                    .create(
                         body=f'Low Price Alert! Only ${price} to fly from {from_city}-{from_code} to {to_city}-{to_code}, from {a_t[0]} to {d_t[0]}',
                         from_='+13203387380',
                         to='+254717143790'
                     )

                print(message.status)



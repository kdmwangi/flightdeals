import requests
from requests.auth import HTTPBasicAuth

endpoint = "https://api.sheety.co/0787d74e4153aa2868fb41900212715e/flightDeals/prices"
response = requests.get(url=endpoint, auth=HTTPBasicAuth('mwangi', 'bnVsbDpudWxs'))
response.raise_for_status()
# print(response.json())
data = response.json()['prices']
# print(data)

kiwi_search_loc = "https://tequila-api.kiwi.com/locations/query"
header = {
    "apikey":"0vsWVLna1emSIMW76eKLvCvgT6WNeR7h"
}
for x in data:
    # print(x['city'])
    req = {
        "term":x['city']
    }
    response = requests.get(url=kiwi_search_loc,headers=header,params=req)
    response.raise_for_status()
    print(response.json()['locations'][0]['code'])
    code = response.json()['locations'][0]['code']
    y = x['id']
    print(y)
    SHEETY_UPDATE_ENDPOINT = f"https://api.sheety.co/c9c4b407ab43ef84bc6a79436df14325/flights/prices/{y}"
    update = {
        'price':{
            "iataCode": code,
        }
    }

    res = requests.put(url=SHEETY_UPDATE_ENDPOINT, auth=HTTPBasicAuth('mwangi', 'bnVsbDpudWxs'), json=update)
    res.raise_for_status()
    print(res.status_code)
# This contains the object-oriented programming approach of the flight deals capstone project
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


to_visit = DataManager()
# print(to_visit.sheets_data())
search_results = FlightSearch()
# print(search_results.searching_flights(to_visit.sheets_data()))
search_data = search_results.searching_flights(to_visit.sheets_data())
lowest_flights = FlightData()
data = lowest_flights.flight_data_str(search_data)
notify = NotificationManager()
send = notify.send_notification(data)
print(send)



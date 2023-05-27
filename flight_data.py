from flight_search import FlightSearch
from notification_manager import NotificationManager

class FlightData:
    #This class is responsible for structuring the flight data.
    def flight_data_str(self, search_data:FlightSearch):
        search_price_result = []
        flight_search_data = search_data
        for flight in flight_search_data[:10]:
            if flight:
                search_price_result.append(flight)
        return search_price_result

        # for x in search_price_result:
        #
        #     # print(x)
        #     for m in range(len(x)):
        #         print(x[m]['flyFrom'])
        #         from_code = x[m]['flyFrom']
        #
        #         print(x[m]['flyTo'])
        #         to_code = x[m]['flyTo']
        #
        #         print(x[m]['cityFrom'])
        #         from_city = x[m]['cityFrom']
        #
        #         print(x[m]['cityTo'])
        #         to_city = x[m]['cityTo']
        #
        #         a_t = x[m]['local_arrival'].split('T')
        #         print(a_t[0])
        #         d_t = x[m]['local_departure'].split('T')
        #         print(d_t[0])
        #         price = x[m]['price']
        #         print(f"${x[m]['price']}")


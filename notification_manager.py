from twilio.rest import Client
# from flight_data import FlightData
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_notification(self, data):
        search_price_result=data
        for x in search_price_result:

            # print(x)
            for m in range(len(x)):
                print(x[m]['flyFrom'])
                from_code = x[m]['flyFrom']

                print(x[m]['flyTo'])
                to_code = x[m]['flyTo']

                print(x[m]['cityFrom'])
                from_city = x[m]['cityFrom']

                print(x[m]['cityTo'])
                to_city = x[m]['cityTo']

                a_t = x[m]['local_arrival'].split('T')
                print(a_t[0])
                d_t = x[m]['local_departure'].split('T')
                print(d_t[0])
                price = x[m]['price']
                print(f"${x[m]['price']}")

                account_sid = "ACf52a092602490fcd210e96d7190fe39d"
                auth_token = "fab84f7d55d29edbc0a00a851750bfd1"
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=f'Low Price Alert! Only ${price} to fly from {from_city}-{from_code} to {to_city}-{to_code}, from {a_t[0]} to {d_t[0]}',
                    from_='+13203387380',
                    to='+254717143790'
                )

                print(message.status)


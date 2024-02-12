# Flight Deals

import custom_logging as logging

from flight_search import FlightSearch

from notification_manager import NotificationManager

from data_manager import DataManager

from datetime import datetime, timedelta

ORIGIN = '-'

COUNTRY = '-'

CURRENCY = 'USD'


def main():

    # Set objects
    data_manager = DataManager()

    flight_finder = FlightSearch()

    notifications = NotificationManager()

    locations = data_manager.get_locations()

    for location in locations:
        # Confirm database has IATA Code
        if not location['iataCode']:
            location['iataCode'] = flight_finder.get_code(location['city'])

            parameters = {
                'price': {
                    'iataCode': location['iataCode']
                }
            }

            data_manager.update_locations(location['id'], parameters)

        # Search for any flights to the current location
        parameters = {
            'fly_from': ORIGIN,
            'fly_to': location['iataCode'],
            'date_from': datetime.now().strftime('%d/%m/%Y'),
            'date_to': (datetime.now() + timedelta(days=180)).strftime('%d/%m/%Y'),
            'return_from': (datetime.now() + timedelta(days=7)).strftime('%d/%m/%Y'),
            'return_to': (datetime.now() + timedelta(days=30)).strftime('%d/%m/%Y'),
            'direct_flights': 1,
            'partner_market': ORIGIN.lower(),
            'curr': CURRENCY,
        }

        flights = flight_finder.find(parameters)['data']

        #  If none, continue with the next location
        if not flights:
            logging.warning(f"No flights from {location['iataCode']} to {ORIGIN} available at the moment.")
            continue

        #  If there's a cheap flight, send SMS notification
        flight_price = flights[0]['price']
        lowest_price = location['lowestPrice']

        if flight_price <= lowest_price:
            notifications.create_sms(flights)
            notifications.send_sms()
        else:
            logging.warning(f"No cheap flights from {location['iataCode']} to {ORIGIN} available at the moment.")


if __name__ == '__main__':
    main()

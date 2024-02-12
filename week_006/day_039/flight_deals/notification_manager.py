import custom_logging as logging

from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.TWILIO_SID = '-'
        self.TWILIO_TOKEN = '-'

        self.PHONE_FROM = '-'
        self.PHONE_TO = '-'

        self.CLIENT = Client(self.TWILIO_SID, self.TWILIO_TOKEN)

        self.sms = ''

    def create_sms(self, flight):
        price = flight[0]['price']
        from_city = flight[0]['cityFrom']
        from_code = flight[0]['flyFrom']
        to_city = flight[0]['cityTo']
        to_code = flight[0]['flyTo']
        departure_date = flight[0]['route'][0]['local_departure'].split('T')[0]
        arrival_date = flight[0]['route'][0]['local_arrival'].split('T')[0]

        self.sms = (f"\nLow Price Alert! Only ${price:,.2f} to fly from"
                    f" {from_city}-{from_code} to {to_city}-{to_code},"
                    f" from {departure_date} to {arrival_date}")

    def send_sms(self):
        logging.info(self.sms)

        self.CLIENT.messages.create(
            from_=self.PHONE_FROM,
            body=self.sms,
            to=self.PHONE_TO
        )

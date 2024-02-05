import requests

from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
ALERT_THRESHOLD = 5.0

AV_API_KEY = "-"
AV_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "-"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MAX_ARTICLES = 1

TWILIO_SID = '-'
TWILIO_TOKEN = '-'

PHONE_FROM = '-'
PHONE_TO = '-'

CLIENT = Client(TWILIO_SID, TWILIO_TOKEN)


def send_request(endpoint: str, **kwargs) -> dict:
    parameters = kwargs

    response = requests.get(endpoint, parameters)

    response.raise_for_status()

    return response.json()


def fetch_news() -> list:
    parameters = {
        'apiKey': NEWS_API_KEY,
        'q': COMPANY_NAME,
        'searchIn': 'title',
        'sortBy': 'popularity',
        'pageSize': MAX_ARTICLES
    }

    return send_request(NEWS_ENDPOINT, **parameters)['articles']


def fetch_stock_data() -> list:
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': AV_API_KEY
    }

    stock_data = send_request(AV_ENDPOINT, **parameters)

    stock_data = [data for data in stock_data['Time Series (Daily)'].values()][:2]

    return [float(data['4. close']) for data in stock_data]


def calculate_stock_difference() -> float:
    closing_data = fetch_stock_data()
    # Return STOCK price difference between yesterday and the day before yesterday
    return (closing_data[0] - closing_data[1]) / closing_data[0] * 100


def build_sms(article: dict) -> str:
    sms = (
            f"{STOCK}: {"🔺" if stock_difference > 0 else "🔻"}{abs(stock_difference)}%\n" +
            f"Headline: {article['title']}\n" +
            f"Brief: {article['description']}\n"
    )

    return sms


def send_sms(sms_body: str):

    CLIENT.messages.create(
        from_=PHONE_FROM,
        body=sms_body,
        to=PHONE_TO
    )


# Main

stock_difference = calculate_stock_difference()

if abs(stock_difference) >= ALERT_THRESHOLD:

    news_articles = fetch_news()

    messages = [build_sms(article) for article in news_articles]

    for message in messages:
        send_sms(message)

else:
    print("\nNothing interesting is going on at the moment.")
    print(f"Stock difference was: {"{:.2f}".format(stock_difference)}%")

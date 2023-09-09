import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
dt = datetime.now()
DATE = dt.date()
today = datetime.today()

YESTERDAY = today - timedelta(days=1)
print(YESTERDAY)
DAY_BEFORE_YESTERDAY = today - timedelta(days=2)
print(DAY_BEFORE_YESTERDAY)

account_sid = "ACde6a306d91521b0dad494b984f42beea"
auth_Token = "1533eabe1b7d6a4db613a6f4ce1830fc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "OLAE3M5O0ZJ559OF"
PARAMETERS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "outputsize": "compact",
    "apikey": "OLAE3M5O0ZJ559OF"
}

PARAMETERS_2 = {
    "q": COMPANY_NAME,
    "from": DATE,
    "sortBy": "popularity",
    "apiKey": "a40fbb5734a34d6b9c94add310498676"
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=STOCK_ENDPOINT, params=PARAMETERS)
print(response)
response.raise_for_status()
stock_data = response.json()["Time Series (60min)"]
data_list = [value for (key, value) in stock_data.items()]
yesterdays_data = data_list[0]
day_before_yesterdays_data = data_list[16]
yesterdays_closing_price = float(yesterdays_data["4. close"])
# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterdays_closing_price = float(day_before_yesterdays_data["4. close"])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = (yesterdays_closing_price - day_before_yesterdays_closing_price)
up_down = None
if positive_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
average = (yesterdays_closing_price + day_before_yesterdays_closing_price)/2
percentage_difference = round((positive_difference/average)*100)

if abs(percentage_difference) > 5:

    response_2 = requests.get(url=NEWS_ENDPOINT, params=PARAMETERS_2)
    news_data = response_2.json()["articles"]
    top_articles = news_data[:3]
    print(top_articles)
    # articles_list = news_data["articles"][:3]
    #
    # print(articles_list["title"]

    new_news_list = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']},\nBrief: {article['description']}" for article in top_articles]


    client = Client(account_sid, auth_Token)
    for article in new_news_list:
        message = client.messages.create(
            body=article,
            from_="+16165233176",
            to="+2349134710006"
        )

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


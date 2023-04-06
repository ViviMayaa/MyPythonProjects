from data_test import api_key_stock, function_time, symbol_stonk, api_key_news, name_stonk
from requests import get
import json
from image import bear,bull


def send():
    try:
        print("Starting API Stocks")
        print(bull)
        url_api_stock = f"https://www.alphavantage.co/query?function={function_time}&symbol={symbol_stonk}&apikey={api_key_stock}"

        result = get(url=url_api_stock)

        stonk_data = result.json()
        # stonk_data = {'Error Message': 'This API function (0) does not exist.'}
        error_value = list(stonk_data.keys())
        dates = list(stonk_data['Time Series (Daily)'].keys())

        url_api_news = f'https://newsapi.org/v2/top-headlines?q={name_stonk}&apiKey={api_key_news}'
        result_news = get(url=url_api_news).json()
        amount_of_news = int(len(result_news['articles']))

        if error_value[0] != 'Error Message':
            past_day_info = stonk_data['Time Series (Daily)'][dates[0]]
            opening_price = past_day_info['1. open']
            closing_price = past_day_info['4. close']
            part = float(closing_price) - float(opening_price)
            percentage = str((float(part) / float(opening_price)) * 100)
            if float(opening_price) <= float(closing_price):
                index = "higher"
            else:
                index = "lower"
            print(f"Here follows the data for {symbol_stonk} {name_stonk.capitalize()} at {dates[0]}\nOpening price was {opening_price}, "
                  f"closing price was {closing_price}\nwith a change of {percentage[:5]}% {index}\n")
            print(f"Latest news related to {name_stonk.capitalize()}:\n")
            for i, _ in enumerate(range(amount_of_news)):
                title = result_news['articles'][i]['title']
                description = result_news['articles'][i]['description']
                url_more_new = result_news['articles'][i]['url']
                print(f"Title of the news: {title}\n{description}\nFor more information access: {url_more_new}")

        else:
            print(f"An error has occurred: {stonk_data['Error Message']}")

    except TimeoutError:
        raise TimeoutError("A Timeout error has occurred, please try again later.")



send()
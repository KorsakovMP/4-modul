# Python program to get the real-time
# currency exchange rate
import requests, json

from config import API_KEY


# Function to get real time currency exchange
def real_time_currency_exchange_rate(from_currency, to_currency):
    # importing required libraries

    # base_url variable store base url
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # main_url variable store complete url
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + API_KEY

    # get method of requests module


    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    return f"Result before parsing the json data :\n {result}"

    # print(" Result before parsing the json data :\n", result)
    #
    # print("\n After parsing : \n Realtime Currency Exchange Rate for",
    #       result["Realtime Currency Exchange Rate"]
    #       ["2. From_Currency Name"], "TO",
    #       result["Realtime Currency Exchange Rate"]
    #       ["4. To_Currency Name"], "is",
    #       result["Realtime Currency Exchange Rate"]
    #       ['5. Exchange Rate'], to_currency)


def get_currency_exchange_rate_from_alfa_bank(currency: str):
    currency = currency.lower()
    # r = requests.get(url='https://alfabank.ru/ext-json/0.2/exchange/cash/?offset=0&limit=2&mode=rest')
    r = requests.get(url=f'https://open.er-api.com/v6/latest/{currency}')
    request = r.json()
    if currency in 'usd, eur, chf, gpb, rub':
        return currency, request.get('rates')
    return 'usd, eur, chf, gpb, rub'


# Driver code
if __name__ == "__main__":
    get_currency_exchange_rate_from_alfa_bank()

    # # currency code
    # from_currency = "USD"
    # to_currency = "SAR"
    #
    # # enter your api key here
    # # Welcome to Alpha Vantage! Your dedicated access key is: TF4DZIC10UR9ICDH. Please record this API key at a safe place for future data access.
    # # api_key = "TF4DZIC10UR9ICDH"
    #
    # # function calling
    # print(real_time_currency_exchange_rate(from_currency, to_currency))
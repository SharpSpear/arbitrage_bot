# import requests

# def fetch_binance_pairs_and_prices():
#     url = 'https://api.binance.com/api/v3/ticker/price'
#     response = requests.get(url)

#     if response.status_code == 200:
#         market_data = response.json()
#         pairs_and_prices = {}

#         for market in market_data:
#             pair = market['symbol']
#             last_traded_price = float(market['price'])
#             pairs_and_prices[pair] = last_traded_price

#         return pairs_and_prices
#     else:
#         print(f"Error: API request failed with status code {response.status_code}")
#         return None

# if __name__ == "__main__":
#     pairs_and_prices = fetch_binance_pairs_and_prices()
#     # print(len(pairs_and_prices))
#     if pairs_and_prices:
#         i = 0
#         for pair, price in pairs_and_prices.items():
#             i += 1
#             if i >= 100:
#                 break
#             formatted_price = format(price, '.8f')
#             print(f"{pair}: {formatted_price}")

# import requests

# api_key = "UW4nvy9odlM2K97fmVdpjDwITiE5qwYEE9mpIvy3pIA5YmhJPhYbN7dHm579611o"
# secret_key = "xNChxJQDRoqq4C7Ojr5TVOLpWCQM9DFtCszjpeWDrxLamcYqytW0eCs2eTusxoEQ"

# headers = {
#     "X-MBX-APIKEY": api_key
# }

# def fetch_binance_account_info():
#     url = "https://api.binance.com/api/v3/account"
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     return data

# if __name__ == "__main__":
#     account_info = fetch_binance_account_info()
#     print(account_info)


# api_key = "UW4nvy9odlM2K97fmVdpjDwITiE5qwYEE9mpIvy3pIA5YmhJPhYbN7dHm579611o"
# api_secret = "xNChxJQDRoqq4C7Ojr5TVOLpWCQM9DFtCszjpeWDrxLamcYqytW0eCs2eTusxoEQ"

# import datetime
# import time
# # Define the start and end times for the data
# end_time = datetime.datetime.now()
# start_time = end_time - datetime.timedelta(days=365)

# start_timestamp = int(start_time.timestamp() * 1000)
# end_timestamp = int(end_time.timestamp() * 1000)
# import requests
# import json

# # Define the Binance API endpoint for K-line data
# endpoint = 'https://api.binance.com/api/v3/klines'

# # Define the parameters for the API request
# symbol = 'BTCUSDT'
# interval = '15m'
# limit = 1000
# params = {'symbol': symbol, 'interval': interval, 'startTime': start_timestamp, 'endTime': end_timestamp, 'limit': limit}

# # Send the API request and store the response data in a list
# data = []
# while True:
#     response = requests.get(endpoint, params=params)
#     klines = json.loads(response.text)
#     data += klines
#     if len(klines) < limit:
#         break
#     params['startTime'] = int(klines[-1][0]) + 1
#     time.sleep(0.1)

# import pandas as pd

# # Create a pandas dataframe with the OHLC data and timestamps
# ohlc_data = [[float(kline[1]), float(kline[2]), float(kline[3]), float(kline[4])] for kline in data]
# df = pd.DataFrame(ohlc_data, columns=['Open', 'High', 'Low', 'Close'])
# timestamps = [datetime.datetime.fromtimestamp(int(kline[0]) / 1000) for kline in data]
# df['Timestamp'] = timestamps
# df.set_index('Timestamp', inplace=True)

# import mplfinance as mpf

# # Define the style for the plot
# style = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 8})

# # Create the OHLC plot
# mpf.plot(df[-50:], type='candle', style=style, title='BTC/USDT OHLC', ylabel='Price ($)')

# from binance.client import Client
# import sys
# sys.path

# api_key = "UW4nvy9odlM2K97fmVdpjDwITiE5qwYEE9mpIvy3pIA5YmhJPhYbN7dHm579611o"
# api_secret = "xNChxJQDRoqq4C7Ojr5TVOLpWCQM9DFtCszjpeWDrxLamcYqytW0eCs2eTusxoEQ"
# client = Client(api_key, api_secret)
# exchange_info = client.get_exchange_info()
# # i = 0
# for s in exchange_info['symbols']:
#     # i+=1
#     # print(s, s['symbol'], i)
#     if s['symbol'] == 'BTCUSDT':
#         print(s)
#         break

import requests
import time
def fetch_binance_last_traded_prices():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    last_traded_prices = fetch_binance_last_traded_prices()
    for item in last_traded_prices:
        # print(f"{item['symbol']}: {item['lastPrice']}")
        if item['symbol'] == 'ETHUSDT':
            print(item['lastPrice'])
            break

if __name__ == "__main__":
    while(1):
        main()
        time.sleep(5)
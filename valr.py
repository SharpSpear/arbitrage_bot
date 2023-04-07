import requests

def fetch_valr_pairs_and_prices():
    url = 'https://api.valr.com/v1/public/marketsummary'
    response = requests.get(url)

    if response.status_code == 200:
        market_data = response.json()
        pairs_and_prices = {}

        for market in market_data:
            pair = market['currencyPair']
            last_traded_price = float(market['lastTradedPrice'])
            pairs_and_prices[pair] = last_traded_price

        return pairs_and_prices
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None

if __name__ == "__main__":
    pairs_and_prices = fetch_valr_pairs_and_prices()
    if pairs_and_prices:
        for pair, price in pairs_and_prices.items():
            formatted_price = format(price, '.8f')
            print(f"{pair}: {formatted_price}")
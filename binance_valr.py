import requests
import time
def get_binance_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)

    if response.status_code == 200:
        market_data = response.json()
        pairs_and_prices = {}

        for market in market_data:
            pair = market['symbol']
            last_traded_price = float(market['lastPrice'])
            pairs_and_prices[pair] = last_traded_price

        return pairs_and_prices
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None

def get_valr_data():
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

def make_profit(binance_data, valr_data):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    base_assets = ['BTC', 'ETH', 'BUSD']

    binance_pairs = set(binance_data.keys())
    valr_pairs = set(valr_data.keys())
    common_pairs = {pair for pair in binance_pairs if pair in valr_pairs}

    # print("Binance pairs:", binance_pairs)
    # print("Valr pairs:", valr_pairs)
    # print("Common pairs:", common_pairs)

    # print("Binance pairs:", binance_pairs, len(binance_pairs))
    # print("Valr pairs:", valr_pairs, len(valr_pairs))
    # print("Common pairs:", common_pairs, len(common_pairs))

    # diff = {}
    # for i in common_pairs:
    #     diff[i] = binance_data[i] - valr_data[i]
    # print("difference value:", diff)

    # for base_asset in base_assets:
    #     for target_asset in common_pairs:
    #         if target_asset.endswith(base_asset):
    #             zar_to_base_asset_pair = f'ZAR{base_asset}'
    #             if zar_to_base_asset_pair not in binance_data:
    #                 continue

    #             zar_to_base_asset_price = binance_data[zar_to_base_asset_pair]
    #             binance_base_to_target_price = binance_data[target_asset]

    #             valr_target_to_zar_pair = f'{target_asset[:-len(base_asset)]}ZAR'
    #             if valr_target_to_zar_pair not in valr_data:
    #                 continue
    #             valr_target_to_zar_price = valr_data[valr_target_to_zar_pair]

    #             final_zar_value = (1 / zar_to_base_asset_price) + binance_base_to_target_price - valr_target_to_zar_price

    #             print(f"Checking ZAR -> {base_asset} -> {target_asset} -> {valr_target_to_zar_pair}: Final ZAR value = {final_zar_value:.8f} ({(final_zar_value - 1) * 100:.2f}% {'gain' if final_zar_value > 1 else 'loss'})")

    for base_asset in base_assets:
        for first_change in binance_pairs:
            if base_asset in first_change and 'ZAR' in first_change:
                if first_change.endswith('ZAR'):
                    first_value = 1.0 / binance_data[first_change]
                elif first_change.startswith('ZAR'):
                    first_value = binance_data[first_change]
                for second_change in binance_pairs:
                    if second_change.endswith(base_asset):
                        temp_asset = second_change[:-len(base_asset)]
                        if f'{temp_asset}ZAR' not in valr_pairs:
                            continue
                        else:
                            if(binance_data[second_change] == 0):
                                continue
                            second_value = first_value / binance_data[second_change]
                            last_value = second_value * valr_data[f'{temp_asset}ZAR']
                            if last_value > 1:
                                print("ZAR->" + base_asset + "("+"{:f}".format(binance_data[f'{base_asset}ZAR']) + ")"+"->" + temp_asset + "("+"{:f}".format(binance_data[f'{temp_asset}{base_asset}']) +")"+ "->ZAR" + "("+"{:f}".format(valr_data[f'{temp_asset}ZAR']) +")"+ ": profit=" + "{:f}".format(last_value-1))
                    elif second_change.startswith(base_asset):
                        temp_asset = second_change[len(base_asset):]
                        if f'{temp_asset}ZAR' not in valr_pairs:
                            continue
                        else:
                            second_value = first_value * binance_data[second_change]
                            last_value = second_value * valr_data[f'{temp_asset}ZAR']
                            if last_value > 1:
                                print("ZAR->" + base_asset + "("+"{:f}".format(binance_data[f'{base_asset}ZAR']) + ")"+"->" + temp_asset + "("+"{:f}".format(binance_data[f'{base_asset}{temp_asset}'])+")" + "->ZAR" + "("+"{:f}".format(valr_data[f'{temp_asset}ZAR']) +")"+ ": profit=" + "{:f}".format(last_value-1))
                for second_change in binance_pairs:
                    if second_change.endswith(base_asset):
                        X_asset = second_change[:-len(base_asset)]
                        for third_change in binance_pairs:
                            if X_asset in third_change:
                                if third_change.startswith(X_asset):
                                    Y_asset = third_change[len(X_asset):]
                                    if f'{Y_asset}ZAR' not in valr_pairs:
                                        continue
                                    else:
                                        if(binance_data[second_change] == 0):
                                            continue
                                        second_value = first_value / binance_data[second_change]
                                        third_value = second_value * binance_data[third_change]
                                        last_value = third_value * valr_data[f'{Y_asset}ZAR']
                                        if last_value > 1:
                                            print("ZAR->" + base_asset + "("+"{:f}".format(binance_data[f'{base_asset}ZAR']) + ")"+"->" + X_asset + "("+"{:f}".format(binance_data[f'{X_asset}{base_asset}']) +")"+ "->"+ Y_asset+ "("+"{:f}".format(binance_data[f'{X_asset}{Y_asset}'])+")"+"->ZAR" + "("+"{:f}".format(valr_data[f'{Y_asset}ZAR']) +")"+ ": profit=" + "{:f}".format(last_value-1))
                                elif third_change.endswith(X_asset):
                                    Y_asset = third_change[:-len(X_asset)]
                                    if f'{Y_asset}ZAR' not in valr_pairs:
                                        continue
                                    else:
                                        if(binance_data[second_change] == 0 or binance_data[third_change] == 0):
                                            continue
                                        second_value = first_value / binance_data[second_change]
                                        third_value = second_value / binance_data[third_change]
                                        last_value = third_value * valr_data[f'{Y_asset}ZAR']
                                        if last_value > 1:
                                            print("ZAR->" + base_asset + "("+"{:f}".format(binance_data[f'{base_asset}ZAR']) + ")"+"->" + X_asset + "("+"{:f}".format(binance_data[f'{X_asset}{base_asset}']) +")"+ "->"+ Y_asset+ "("+"{:f}".format(binance_data[f'{Y_asset}{X_asset}'])+")"+"->ZAR" + "("+"{:f}".format(valr_data[f'{Y_asset}ZAR']) +")"+ ": profit=" + "{:f}".format(last_value-1))
 
                    elif second_change.startswith(base_asset):
                        X_asset = second_change[len(base_asset):]
                        for third_change in binance_pairs:
                            if X_asset in third_change:
                                if third_change.startswith(X_asset):
                                    Y_asset = third_change[len(X_asset):]
                                    if f'{Y_asset}ZAR' not in valr_pairs:
                                        continue
                                    else:
                                        second_value = first_value * binance_data[second_change]
                                        third_value = second_value * binance_data[third_change]
                                        last_value = third_value * valr_data[f'{Y_asset}ZAR']
                                        if last_value > 1:
                                            print("ZAR->" + base_asset + "("+"{:f}".format(binance_data[f'{base_asset}ZAR']) + ")"+"->" + X_asset + "("+"{:f}".format(binance_data[f'{base_asset}{X_asset}']) +")"+ "->"+ Y_asset+ "("+"{:f}".format(binance_data[f'{X_asset}{Y_asset}'])+")"+"->ZAR" + "("+"{:f}".format(valr_data[f'{Y_asset}ZAR']) +")"+ ": profit=" + "{:f}".format(last_value-1))
                                elif third_change.endswith(X_asset):
                                    Y_asset = third_change[:-len(X_asset)]
                                    if f'{Y_asset}ZAR' not in valr_pairs:
                                        continue
                                    else:
                                        if(binance_data[third_change] == 0):
                                            continue
                                        second_value = first_value * binance_data[second_change]
                                        third_value = second_value / binance_data[third_change]
                                        last_value = third_value * valr_data[f'{Y_asset}ZAR']
                                        if last_value > 1:
                                            print("ZAR->" + base_asset + "("+"{:f}".format(binance_data[f'{base_asset}ZAR']) + ")"+"->" + X_asset + "("+"{:f}".format(binance_data[f'{base_asset}{X_asset}']) +")"+ "->"+ Y_asset+ "("+"{:f}".format(binance_data[f'{Y_asset}{X_asset}'])+")"+"->ZAR" + "("+"{:f}".format(valr_data[f'{Y_asset}ZAR']) +")"+ ": profit=" + "{:f}".format(last_value-1))
 
def _main():

    binance_data = get_binance_data()
    valr_data = get_valr_data()

    # binance_pairs = set(binance_data.keys())
    # for i in valr_data:
    #     if 'BTCZAR' in i:
    #         print(i, binance_data[i])
    if binance_data and valr_data:
        make_profit(binance_data, valr_data)

if __name__ == "__main__":
    while True:
        _main() 
        time.sleep(10)
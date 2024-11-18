import requests

heads = {
'x-cg-demo-api-key': 'CG-7rziM2j3pq2VoT6Uftg5KzyE'

    }


def get_coin_ids():
    r = requests.get('https://api.coingecko.com/api/v3/global', headers=heads)
    coin_list = r.json()
    market_coin_list = list(coin_list['data']['total_market_cap'].keys())

    r = requests.get('https://api.coingecko.com/api/v3/coins/list', headers=heads)

    market_coin_names = []
    market_coin_ids = []

    for coin in r.json():
        for market_coin in market_coin_list:
            if coin['symbol'] == market_coin:
           #     temp_dict = {'name': coin['name'], 'id': coin['id']}
                market_coin_names.append(coin['name'])
                market_coin_ids.append(coin['id'])

 #   print(market_coins)
    return market_coin_names, market_coin_ids

   

import requests

heads = {
'x-cg-demo-api-key': 'CG-7rziM2j3pq2VoT6Uftg5KzyE'

    }

cryptos = [
    'bitcoin', 'ethereum', 'tether', 'solana', 'bnb', 'xrp', 'dogecoin', 'usdc', 'shiba inu', 'peanut the squirrel', 'litecoin'
]



def get_coin_ids():
    r = requests.get('https://api.coingecko.com/api/v3/coins/list', headers=heads)

    market_coin_names = []
    market_coin_ids = []

    for coin in r.json():
        for market_coin in cryptos:
            if coin['name'].lower() == market_coin:
                
                market_coin_names.append(coin['name'])
                market_coin_ids.append(coin['id'])

 #   print(market_coins)
    return market_coin_names, market_coin_ids

   

import requests

heads = {
'x-cg-demo-api-key': 'CG-7rziM2j3pq2VoT6Uftg5KzyE'

    }

top_30_cryptos = [
    "btc", "eth", "usdt", "bnb", "xrp", "ada", "doge", "sol", "matic", 
    "ltc",  "shib", "trx", "uni", "ton", "link", "xlm", "atom", 
    "pepe", "hbar", "fil", "vet", "ftm", "bch"
]



def get_coin_ids():
    r = requests.get('https://api.coingecko.com/api/v3/coins/list', headers=heads)

    market_coin_names = []
    market_coin_ids = []

    for coin in r.json():
        for market_coin in top_30_cryptos:
            if coin['symbol'] == market_coin:
           #     temp_dict = {'name': coin['name'], 'id': coin['id']}
                temp_name = coin['name']
                for coin_id in market_coin_ids:
                    if coin['id'] == coin_id:
                        continue
                if temp_name.lower().find('osmosis') != -1:
                    continue
                
                if market_coin == 'pepe' and temp_name.lower() != 'pepe':
                    continue

                if market_coin == 'doge' and temp_name.lower() != 'doge':
                    continue
                if temp_name.find('(') != -1 or temp_name.lower().find('on') != -1 or temp_name.find('-') != -1 or temp_name.find('69') != -1:
                    continue
                market_coin_names.append(temp_name)
                market_coin_ids.append(coin['id'])

 #   print(market_coins)
    return market_coin_names, market_coin_ids

   

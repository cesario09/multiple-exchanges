from constants import *
from bitex import GDAX, Bitfinex, Bittrex, Poloniex, Bitstamp, Kraken
import time;


#####################
# Exchange reader   #
#####################

def read_prices_from_gdax(pair):
    x = GDAX()
    response = x.ticker(pair)
    try:
        return True, float(response.json()['bid']), float(response.json()['ask'])
    except:
        return False, 0,0

def read_prices_from_bitfinex(pair):
    x = Bitfinex()
    response = x.ticker(pair)
    try:
    	return True, float(response.json()['bid']), float(response.json()['ask'])
    except:
        return False, 0,0

def read_prices_from_bittrex(pair):
    x = Bittrex()
    response = x.ticker(pair)
    try:
        return True, response.json()['result'][0]['Bid'], response.json()['result'][0]['Ask']
    except:
        return False, 0,0

def read_prices_from_poloniex(pair):
    x = Poloniex()
    response = x.ticker(pair)
    try:
        return True, float(response.json()[pair]['highestBid']), float(response.json()[pair]['lowestAsk']) 
    except:
        return False, 0,0

def read_prices_from_bitstamp(pair):
    x = Bitstamp()
    response = x.ticker(pair)
    try:
        return True, float(response.json()['bid']), float(response.json()['ask'])
    except:
        return False, 0,0

def read_prices_from_kraken(pair):
    x = Kraken()
    response = x.ticker(pair)
    try:
        responseList = list(response.json()['result'].values())
        return True, float(responseList[0]['b'][0]), float(responseList[0]['a'][0])    
    except:
        return False, 0,0

def read_prices_from_exchange(exchange, cc):
    
    try:
        pair = currencyMap[exchange][cc['quote']] + currencySeparator[exchange] + currencyMap[exchange][cc['base']]
        pairReversed = currencyMap[exchange][cc['base']] + currencySeparator[exchange] + currencyMap[exchange][cc['quote']]
    except:
        return False, 0,0
    if exchange == 'gdax':
        try:
            return read_prices_from_gdax(pair)
        except:
            try:
                return read_prices_from_gdax(pairReversed)
            except:
                return False, 0,0
    elif exchange == 'bitfinex':
        try:
            return read_prices_from_bitfinex(pair)
        except:
            try:
                return read_prices_from_bitfinex(pairReversed)
            except:
                return False, 0,0
    elif exchange == 'bittrex':
        try:
            return read_prices_from_bittrex(pair)
        except:
            try:
                return read_prices_from_bittrex(pairReversed)
            except:
                return False, 0,0
    elif exchange == 'poloniex':
        try:
            return read_prices_from_poloniex(pair)
        except:
            try:
                return read_prices_from_poloniex(pairReversed)
            except:
                return False, 0,0
    elif exchange == 'bitstamp':
        try:
            return read_prices_from_bitstamp(pair)
        except:
            try:
                return read_prices_from_bitstamp(pairReversed)
            except:
                return False, 0,0
    elif exchange == 'kraken':
        try:
            return read_prices_from_kraken(pair)
        except:
            try:
                return read_prices_from_kraken(pairReversed)
            except:
                return False, 0,0


#####################
# Main     Function #
#####################
def step():
  
    for pair in currencies_pairs:
        first_exchange = True
        found_arbitragem = False
        pp = pair['quote'] + '_' + pair['base']
        f.write(pp + '\n')
        for ee in exchanges:
            

            response, bid, ask = read_prices_from_exchange(ee, pair)

            if response == False:
                continue

            if first_exchange:
                best_bid = bid
                best_ask = ask
                cheap_exchange = ee
                expensive_exchange = ee
                first_exchange = False 
                
            else:
                if bid > best_bid:
                    best_bid = bid
                    expensive_exchange = ee
                    found_arbitragem = True
                if ask < best_ask:
                    best_ask = ask
                    cheap_exchange = ee
                    found_arbitragem = True

        if found_arbitragem:
            pnl = (best_bid - best_ask) / best_ask

            if pnl > 0.05: # ARBITRAGEM!!!!!!!!!!
                message = ("Arbitrage spotted\nPair: {}\n"
                           "Buy on {} at net {}\n"
                           "Sell on {} at net {}\n"
                           "Profit margin of {:.1%}\n".format(pp, cheap_exchange, best_ask,
                                                              expensive_exchange, best_bid, pnl))

                print (message)
                f.write(message)

ts = time.time()
f = open('output' + str(ts) + '.txt','w')

if __name__ == "__main__":
    
    step()
    print("Done")
    f.close()
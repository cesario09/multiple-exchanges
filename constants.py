#####################
# Main 				#
#####################

exchanges = ['gdax', 'bittrex', 'poloniex', 'bitstamp', 'kraken']
#exchanges = ['gdax', 'bittrex', 'bitstamp']
currencies = ['BTC','ETH','LTC','XRP', 'DASH', 'XEM', 'XMR', 'BCH']
#currencies = ['BTC','LTC','ETH']

#####################
# Define pairs      #
#####################

currencies_pairs = [{'quote': x, 'base':y} for x in currencies for y in currencies if x!=y]

#####################
# Currency Mapping  #
#####################

currencySeparator = {}
currencyMap = {}

currencySeparator['gdax'] = '-'
currencyMap['gdax'] = {}
currencyMap['gdax']['BTC'] = 'BTC'
currencyMap['gdax']['ETH'] = 'ETH'
currencyMap['gdax']['LTC'] = 'LTC'
currencyMap['gdax']['XRP'] = 'XRP'
currencyMap['gdax']['USD'] = 'USD'
currencyMap['gdax']['DASH'] = 'DASH'
currencyMap['gdax']['XEM'] = 'XEM'
currencyMap['gdax']['XMR'] = 'XMR'
currencyMap['gdax']['BCH'] = 'BCH'

currencySeparator['bitfinex'] = ''
currencyMap['bitfinex'] = {}
currencyMap['bitfinex']['BTC'] = 'btc'
currencyMap['bitfinex']['ETH'] = 'eth'
currencyMap['bitfinex']['LTC'] = 'ltc'
currencyMap['bitfinex']['XRP'] = 'xrp'
currencyMap['bitfinex']['USD'] = 'usd'
currencyMap['bitfinex']['XMR'] = 'xmr'
currencyMap['bitfinex']['BCH'] = 'bch'

currencySeparator['bittrex'] = '-'
currencyMap['bittrex'] = {}
currencyMap['bittrex']['BTC'] = 'BTC'
currencyMap['bittrex']['ETH'] = 'ETH'
currencyMap['bittrex']['LTC'] = 'LTC'
currencyMap['bittrex']['XRP'] = 'XRP'
currencyMap['bittrex']['USD'] = 'USDT'
currencyMap['bittrex']['DASH'] = 'DASH'
currencyMap['bittrex']['XEM'] = 'XEM'
currencyMap['bittrex']['XMR'] = 'XMR'

currencySeparator['poloniex'] = '_'
currencyMap['poloniex'] = {}
currencyMap['poloniex']['BTC'] = 'BTC'
currencyMap['poloniex']['ETH'] = 'ETH'
currencyMap['poloniex']['LTC'] = 'LTC'
currencyMap['poloniex']['XRP'] = 'XRP'
currencyMap['poloniex']['USD'] = 'USDT'
currencyMap['poloniex']['DASH'] = 'DASH'
currencyMap['poloniex']['XEM'] = 'XEM'
currencyMap['poloniex']['XMR'] = 'XMR'
currencyMap['poloniex']['BCH'] = 'BCH'

currencySeparator['bitstamp'] = ''
currencyMap['bitstamp'] = {}
currencyMap['bitstamp']['BTC'] = 'btc'
currencyMap['bitstamp']['ETH'] = 'eth'
currencyMap['bitstamp']['LTC'] = 'ltc'
currencyMap['bitstamp']['XRP'] = 'xrp'
currencyMap['bitstamp']['USD'] = 'usd'
currencyMap['bitstamp']['BCH'] = 'bch'

currencySeparator['kraken'] = ''
currencyMap['kraken'] = {}
currencyMap['kraken']['BTC'] = 'XBT'
currencyMap['kraken']['ETH'] = 'ETH'
currencyMap['kraken']['LTC'] = 'LTC'
currencyMap['kraken']['XRP'] = 'XRP'
currencyMap['kraken']['USD'] = 'USD'
currencyMap['kraken']['DASH'] = 'DASH'
currencyMap['kraken']['XMR'] = 'XMR'
currencyMap['kraken']['BCH'] = 'BCH'
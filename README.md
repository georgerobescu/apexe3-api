# APEXE3-API-PYTHON - Real-time & On-demand Digital Asset Analytics & Trading
A Python wrapper to access powerful analytics generated by APEX:E3's Big Data Analytics Architecture

### [Install](#install) · [Quick Start](#quickstart) · [Examples](#examples) · [API Docs](#apiDocs) · [Social](#social)

In addition to enriched exchange data from all major cryptocurrency exchanges, the **APEX:E3 API** includes real-time analytics and market intelligence. This means you can access live orderbook analytics, arbitrage opportunities and identify large blocks of liquidity with ease. The low code examples have been designed with simplicity in mind so that you can start to manipulate the data to enhance or create new trading bots, conduct real-time analysis or create powerful algorithms. The data structures can be easily stored in your database of choice for historical analysis, backtesting or general querying.

This API has been created for quants, algorithmic traders, data scientists, financial analysts and anybody who has a casual or formal interest in creating real-time trading algorithms or cryptocurrency markets research. 

Current real-time and on-demand features:

- structured data from all the major cryptocurrency exchanges covering thousands of pairs
- sorted aggregated global orderbook data structure (bids/asks for individual pairs across multiple exchanges in one place)  
- bid/ask imbalance ratios (quantification of buy / sell market intent)
- orderbook whale detection (identification of abnormally large bids across thousands of markets)
- arbitrage opportunities (between multiple exchanges and thousands of markets in one place) 
- spreads (delta between top bid and ask prices across thousands of markets)

## Supported Cryptocurrency Exchanges

|      |Exchange|
|------|--------|
|[![binance](https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg)](https://www.binance.com)|Binance|
|[![binance](https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg)](https://www.binance.com)|Binance Futures |
|[![bitfinex](https://user-images.githubusercontent.com/1294454/27766244-e328a50c-5ed2-11e7-947b-041416579bb3.jpg)](https://www.bitfinex.com)|Bitfinex|  
|[![bitmex](https://user-images.githubusercontent.com/1294454/27766319-f653c6e6-5ed4-11e7-933d-f0bc3699ae8f.jpg)](https://www.bitmex.com)|Bitmex| 
|[![bitstamp](https://user-images.githubusercontent.com/1294454/27786377-8c8ab57e-5fe9-11e7-8ea4-2b05b6bcceec.jpg)](https://www.bitstamp.net)|Bitstamp|
|[![bittrex](https://user-images.githubusercontent.com/51840849/87153921-edf53180-c2c0-11ea-96b9-f2a9a95a455b.jpg)](https://bittrex.com)|Bittrex|  
|[![coinbasepro](https://user-images.githubusercontent.com/1294454/41764625-63b7ffde-760a-11e8-996d-a6328fa9347a.jpg)](https://pro.coinbase.com/)|Coinbase Pro|  
|[![ftx](https://user-images.githubusercontent.com/1294454/67149189-df896480-f2b0-11e9-8816-41593e17f9ec.jpg)](https://ftx.com)|FTX|
|[![ftx](https://user-images.githubusercontent.com/1294454/67149189-df896480-f2b0-11e9-8816-41593e17f9ec.jpg)](https://ftx.com)|FTX Derivatives|
|[![gateio](https://user-images.githubusercontent.com/1294454/31784029-0313c702-b509-11e7-9ccc-bc0da6a0e435.jpg)](https://www.gate.io)|Gateio|
|[![hitbtc](https://user-images.githubusercontent.com/1294454/27766555-8eaec20e-5edc-11e7-9c5b-6dc69fc42f5e.jpg)](https://hitbtc.com)|HitBTC|
|[![huobipro](https://user-images.githubusercontent.com/1294454/76137448-22748a80-604e-11ea-8069-6e389271911d.jpg)](https://www.huobi.com/en-us)|HuobiPRO|
|[![kraken](https://user-images.githubusercontent.com/51840849/76173629-fc67fb00-61b1-11ea-84fe-f2de582f58a3.jpg)](https://www.kraken.com)|Kraken|
|[![kraken](https://user-images.githubusercontent.com/51840849/76173629-fc67fb00-61b1-11ea-84fe-f2de582f58a3.jpg)](https://www.kraken.com)|Kraken Futures|
|[![okex](https://user-images.githubusercontent.com/1294454/32552768-0d6dd3c6-c4a6-11e7-90f8-c043b64756a7.jpg)](https://www.okex.com)|OKEX|
|[![okex](https://user-images.githubusercontent.com/1294454/32552768-0d6dd3c6-c4a6-11e7-90f8-c043b64756a7.jpg)](https://www.okex.com)|OKEX Derivatives|
|[![poloniex](https://user-images.githubusercontent.com/1294454/27766817-e9456312-5ee6-11e7-9b3c-b628ca5626a5.jpg)](https://poloniex.com)|Poloniex| 
|[![zb](https://user-images.githubusercontent.com/1294454/32859187-cd5214f0-ca5e-11e7-967d-96568e2e2bd1.jpg)](https://www.zb.com)|ZB|

## Install

Tested successfully using Python 3.8.x. (You may have to use sudo depending on how your local permissions are set).

1. Clone it into your project directory from [APEX:E3 GitHub repository](https://github.com/apexe3/apexe3-api-python):
```shell
git clone git@github.com:apexe3/apexe3-api-python.git
```
2. cd into the directory
```shell
cd apexe3-api-python
```
3. run setup.py to install dependencies
```shell
python setup.py install 
```

## Quick start

To stream the global orderbook for BTC/USDT across all supported exchanges type

```shell
python examples/real_time_global_orderbook.py
```
**this will produce a structured dataframe with the top 25 depth for btc/usdt taken from each exchange, combined and ordered to produce a globally updating orderbook ready for real-time algorithmic trading or analysis.**


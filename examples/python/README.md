# APEX:E3 - API Python Low Code Examples

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/python/apexe3/assets/liquidityRealtimeUpdates.gif)

All examples make use of the apexe3/apexe3.py wrapper which implements a subset of the  REST and websocket API definitions defined in the [APEX:E3 API documentation](https://api.ae3platform.com/docs). 

## The Real-time Global Orderbook for any Pair Across Exchanges

To run: 

```shell
python examples/python/real_time_global_orderbook.py
```
This will output the global orderbooks for bids and asks, by best bid and ask prices respectively (only bids are shown for the sake of example).

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/python/apexe3/assets/globalOrderbookUpdating.png)

**As the picture above shows, the top 25 depth for btc/usdt is taken from each exchange, combined and ordered to produce a globally updating orderbook ready for real-time algorithmic trading or analysis.** 

The initialise_global_orderbook function initialises the global orderbook with BTC/USDT SPOT market. You can change "btc", "usdt" to a pair of your choice. (Derivatives (SWAP, FUTURE) are also supported).
```python
    initialise_global_orderbook("btc", "usdt", None,"SPOT")
```

In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges in real-time.**

- bid price (bid px) (ordered by best bid across exchanges).
- bid size 
- cumulative bid size (bid size added up at each depth)
- bid sum (bid px * bid size)
- cumulative bid sum are retrieved (bid sum added up at each depth)
- exchange

All updates are emitted and converted to a pandas dataframe for further programmatic analysis.
```python
    emitter.on('GLOBAL_ORDERBOOK', process_global_orderbook)
```
You can easily access the structured dataframe as it updates in real-time in the process_global_orderbook function.

```python
def process_global_orderbook(event):
    table=pd.DataFrame(event["bids"])
    table.columns = ['bid px', 'bid size', 'bid size cumulative', 'bid sum', 'bid sum cumulative', 'exchange']    
```
You can easily process the table of bids (or asks) in your trading algorithm logic, store it for historical analysis or manipulate as desired.

## Smart Order Routing Analytics - The Real-time Total Supply & Demand of Liquidity for any Pair Across Exchanges

To run: 

```shell
python examples/python/real_time_global_liquidity.py
```

This will output the total demand (bid) and supply (ask) liquidity for the BTC/USDT Spot market. 
![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/python/apexe3/assets/globalLiquidityExample.png?raw=true)

The above picture shows a real-time aggregation of the top 25 depth of BTC/USDT Spot markets across supported exchanges. 
In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges in real-time.**

- Exchange
- Ask Liqudity (The total USDT amount available to buy on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Bid Liqudity (The total USDT in demand on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Amount (The amount of BTC available to buy on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Imbalance (Ask Liquidity - Bid Liquidity)
- Market Price_25 (The likely price of a market order filling the top 25 orders on that exchange)


All updates are emitted and converted to a pandas dataframe for further programmatic analysis.

```python
 emitter.on('LIVE_LIQUIDITY', process_liquidity_update)
 ```

You can easily access the structured dataframe as it updates in real-time in the process_global_orderbook function.
```python
def process_liquidity_update(event):
    table=pd.DataFrame(event)
    table.columns = ['Exchange', 'Ask Liquidity', 'Bid Liquidity', 'Amount', 'Imbalance', 'Market Price_25']
```
**You can easily process this table in your trading algorithm, smart order routing logic, store it for historical analysis or manipulate as desired.**

## Identify Whale Orders, Arbitrage Opportunities, Large/Medium/Small Bid/Ask Imbalances & Tightest spreads for any Pair Across Exchanges

To run:

```shell
python examples/python/real_time_insights.py
```
This will output spreads for BTC/USDT, ranked by tightest spread for a given exchange.

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/python/apexe3/assets/spreadsAcrossExchanges.png?raw=true)

Uncommenting the following block, will produce similarly structured tables for whale orders, bid/ask order imbalances and arbitrage opportunities.

```python
    #UNCOMMENT TO RECIEVE UPDATES FOR THESE ANALYTICS
    #emitter.on('WHALE', process_whales)
    #emitter.on('VOI_BID', process_bid_imbalances)
    #emitter.on('VOI_ASK', process_ask_imbalances)
    #emitter.on('ARBITRAGE', process_arbitrage)
```
**You can easily process these table in your trading algorithm, or store them to analyse how orderbook whales, spreads, imbalances and arbitrage opportunities evolve over time **



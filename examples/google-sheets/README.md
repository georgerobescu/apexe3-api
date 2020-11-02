# APEX:E3 - API Google Sheet Low Code Examples

![preview](h)

All examples make use of the apexe3.gs wrapper script which implements a subset of the REST and websocket API definitions defined in the [APEX:E3 API documentation](https://api.ae3platform.com/docs). 

**Please contact contactus@apexe3.com to get access to this spreadsheet.** 

You can easily manipulate the data contained in all sheets to create derived columns or charts.

## The On-Deman Global Orderbook for any Pair Across Exchanges

This shows the global orderbooks for bids and asks, by best bid and ask prices respectively (only bids are shown for the sake of example).

![preview]()

**As the picture above shows, the top 25 depth for btc/usdt is taken from each exchange, combined and ordered to produce a globally updating orderbook ready for real-time algorithmic trading or analysis.** 


In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges when clicking refresh.**

- bid price (bid px) (ordered by best bid across exchanges).
- bid size 
- cumulative bid size (bid size added up at each depth)
- bid sum (bid px * bid size)
- cumulative bid sum are retrieved (bid sum added up at each depth)
- exchange



## Smart Order Routing Analytics - The Real-time Total Supply & Demand of Liquidity for any Pair Across Exchanges


This shows the total demand (bid) and supply (ask) liquidity for the BTC/USDT Spot market. 
![preview]()

The above picture shows an up-to-date aggregation of the top 25 depth of BTC/USDT Spot markets across supported exchanges. 
In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges in real-time.**

- Exchange
- Ask Liqudity (The total USDT amount available to buy on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Bid Liqudity (The total USDT in demand on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Amount (The amount of BTC available to buy on the relevant exchange at that moment in time. This is based on the top 25 depth)
- Imbalance (Ask Liquidity - Bid Liquidity)
- Market Price_25 (The likely price of a market order filling the top 25 orders on that exchange)


## Screen markets using technical indicators for any Pair, Quote or Exchange

This shows screened results for BTC/USDT consisting of price and volume metrics on an on-demand basis.

![preview]()

This example screens the BTC/USDT pair using the following code:

A successful response will consist of the following columns:

- exchangeId
- baseId 
- quoteId
- v24HrChange (24 hour volume change)
- v30dChg (30 day volume change)
- v24HrVsV30dSum (24 hour vs 30 day volume change)
- p15MinChg (15 minute price change)
- p1HrChg (1 hour price change)
- p7dChg (7 day price change)
- pLast (latest price)


The input form allows for instantly screening pairs, markets or exchanges by RSI, Moving Average, Volatility, Bollinger Bands, Fibretracement, Trends and Ichimoku cloud technical indicator analysis.

Example values can be found by hovering over the input form fields.
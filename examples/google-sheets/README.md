# APEX:E3 - API Google Sheet Low Code Examples

All examples make use of the apexe3.gs wrapper script which implements a subset of the REST and websocket API definitions defined in the [APEX:E3 API documentation](https://api.ae3platform.com/docs). 

**Please contact contactus@apexe3.com to get access to this spreadsheet.** 

You can easily manipulate the data contained in all sheets to create derived columns or charts.

## The On-Demand Global Orderbook & Liquidity for any Pair Across Exchanges

This shows the global orderbooks for bids and asks, by best bid and ask prices respectively (only bids are shown for the sake of example).

Global liquidity based on aggregatd top 25 orderbook depth is also shown.

The form on the top left can be used to select other pairs.

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/google-sheets/assets/gsheetGlobalOrderbook.png?raw=true)

**As the picture above shows, the top 25 depth for btc/usdt is taken from each exchange, combined and ordered to produce a globally updating orderbook ready for real-time algorithmic trading or analysis.** 


In this example, the following columns **are retrieved for every BTC/USDT orderbook update across supported exchanges when clicking refresh.**

- bid price (bid px) (ordered by best bid across exchanges).
- bid size 
- cumulative bid size (bid size added up at each depth)
- bid sum (bid px * bid size)
- cumulative bid sum are retrieved (bid sum added up at each depth)
- exchange



## Screen markets using technical indicators for any Pair, Quote or Exchange

This shows screened results for BTC/USDT consisting of price and volume metrics on an on-demand basis.

![preview](https://github.com/apexe3/apexe3-api/blob/main/examples/google-sheets/assets/ScreenerGS.png?raw=true)

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

Example values can be found by hovering over the input form fields on the top left.

# APEX:E3 - API Python Low Code Examples

![preview](https://raw.githubusercontent.com/apexe3/apexe3-api-python/main/apexe3/assets/liquidityRealtimeUpdates.gif)

All examples make use of the apexe3/apexe3.py wrapper which implements a subset of the  REST and websocket API definitions defined in the [APEX:E3 API documentation](https://api.ae3platform.com/docs). 

## The Real-time Global Orderbook - examples/real_time_global_orderbook.py

To run: 

```shell
python examples/real_time_global_orderbook.py
```
This will output the global orderbooks for bids and asks, both ordered by best bid and ask prices respectively (only bids are shown for the sake of example).

![preview](https://github.com/apexe3/apexe3-api-python/blob/main/apexe3/assets/globalOrderbookUpdating.png?raw=true)

The initialise_global_orderbook function initialises the global orderbook with BTC/USDT SPOT market. You can change "btc", "usdt" to a pair of your choice. (Derivatives (SWAP, FUTURE) are also supported).
```python
    initialise_global_orderbook("btc", "usdt", None,"SPOT")
```

In this example, the following columns

- bid price (bid px) (ordered by best bid across exchanges).
- bid size 
- cumulative bid size
- bid sum (bid px * bid size)
- cumulative bid sum are retrieved
- exchange

are retrived for every BTC/USDT orderbook update across supported exchanges in real-time. 

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

Your APEX:E3 credentials will need to be set in the init() function. (email contactus@apexe3.com to obtain credentials).

```python
    clientId = "your-client-id-goes-here"
    clientSecret = "your-client-secret-goes-here"
```




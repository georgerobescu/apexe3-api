'''
/**
 * real_time_liquidity.py
 * 
 * Streams a real-time liquidity metrics for the supplied pair
 * This data can be used to help with smart order routing 
 * across exchanges.
 * An example use of this data can be found here:
 * https://www.linkedin.com/pulse/apexe3-digital-asset-liqudity-locator-usman-khan
 * 
 * Disclaimer:
 * APEX:E3 is a financial technology company based in the United Kingdom https://www.apexe3.com
 *  
 * None of this code constitutes financial advice. APEX:E3 is not 
 * liable for any loss resulting from the use of this code or the API. 
 * 
 * This code is governed by The MIT License (MIT)
 * 
 * Copyright (c) 2020 APEX:E3 Team
 * 
 **/

'''

import sys
sys.path.append('..')
from apexe3.apexe3 import initialise
from apexe3.apexe3 import initialise_stream
from apexe3.apexe3 import initialise_global_orderbook

import pandas as pd

def process_liquidity_update(event):
    table=pd.DataFrame(event)
    table.columns = ['Exchange', 'Ask Liquidity', 'Bid Liquidity', 'Amount', 'Imbalance', 'Market Price_25']
    #print(' ')
    #print('Liquidity based on top 25 ask depth')
    print(table, end=('\r'))

def process_liquidity_stats_update(event):
    table=pd.DataFrame(event)
    table.columns = ['Total Ask Liquidity', 'Total Amount', 'Total Imbalance']
    #print(' ')
    #print('Liquidity Stats based on top 25 ask depth')
    #print(table)    


def init():
    clientId = "your-client-id-goes-here"
    clientSecret = "your-client-secret-goes-here"
    emitter = initialise(clientId, clientSecret)
    emitter.on('LIVE_LIQUIDITY', process_liquidity_update)
    emitter.on('LIVE_LIQUIDITY_STATS', process_liquidity_stats_update)
    pd.set_option('display.float_format', lambda x: '%.5f' % x)


if __name__ == "__main__":
    init()
    initialise_global_orderbook("btc", "usdt", None,"SPOT")
    

  
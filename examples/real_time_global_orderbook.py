'''
/**
 * real_time_global_orderbook.py
 * 
 * Streams a real-time orderbook for the supplied pair
 * An example of the real-time orderbook is available here:
 * https://app.ae3platform.com/markets/p/BTC/USDT
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
    #Cumulative has a bug - only show bid px  bid size  bid sum
def process_global_orderbook(event):
    table=pd.DataFrame(event["bids"])
    table.columns = ['bid px', 'bid size', 'bid size cumulative', 'bid sum', 'bid sum cumulative', 'exchange']
    print(table)
    table=pd.DataFrame(event["asks"])
    table.columns = ['ask px', 'ask size', 'ask size cumulative', 'ask sum', 'ask sum cumulative', 'exchange']
    print(table)


def init():
    clientId = "client-fund"
    clientSecret = "4fcede79-1699-4e0a-aa54-4f7ab8514d94"
    emitter = initialise(clientId, clientSecret)
    emitter.on('GLOBAL_ORDERBOOK', process_global_orderbook)


if __name__ == "__main__":
    init()
    #Change these values to a base or quote you are interested in
    initialise_global_orderbook("btc", "usdt", None,"SPOT")
    

  
'''
/**
 * real_time_insights.py
 * 
 * Streams a real-time insights for the supplied pair
 * An example of the real-time insights is available here:
 * https://app.ae3platform.com/insights
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
from apexe3.apexe3 import initialise_insights_for_pair

import pandas as pd

#Change these values to a base or quote you are interested in
base = 'btc'
quote = 'usdt'

def process_spread(event):
    print('Best spreads for ' + str(base) +' '+ str(quote))
    table=pd.DataFrame(event["values"])
    table.columns = ['exchange','base','quote','misc','strSpread', 'spread']
    table = table[['exchange','spread']]
    print(table)
    print('------------------------------------------')

def process_whales(event):
    print('Largest whales for ' + str(base) +' '+ str(quote))
    table=pd.DataFrame(event["values"])
    table.columns = ['exchange','base','quote','misc','strSize (USD)', ' size (usd)']
    table = table[['exchange','size (usd)']]
    print(table)
    print('------------------------------------------')

def process_bid_imbalances(event):
    table=pd.DataFrame(event["values"])
    print('bid imbalance for ' + str(base) +' '+ str(quote))
    table.columns = ['exchange','base','quote','misc','strStrength (USD)', 'bid imbalance']
    table = table[['exchange','bid imbalance']]
    print(table)
    print('------------------------------------------')

def process_ask_imbalances(event):
    table=pd.DataFrame(event["values"])
    print('ask imbalance for ' + str(base) +' '+str(quote))
    table.columns = ['exchange','base','quote','misc','strStrength (USD)', 'ask imbalance']
    table = table[['exchange','ask imbalance']]
    print(table)
    print('------------------------------------------') 


def init():
    clientId = "client-fund"
    clientSecret = "4fcede79-1699-4e0a-aa54-4f7ab8514d94"
    emitter = initialise(clientId, clientSecret)
    emitter.on('SPREAD', process_spread)
    
    #UNCOMMENT TO RECIEVE UPDATES FOR THESE ANALYTICS
    #emitter.on('WHALE', process_whales)
    #emitter.on('VOI_BID', process_bid_imbalances)
    #emitter.on('VOI_ASK', process_ask_imbalances)


if __name__ == "__main__":
    init()
    initialise_insights_for_pair(base, quote)
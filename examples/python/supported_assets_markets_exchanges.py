'''
/**
 * supported_assets_markets_exchanges.py
 * 
 * Retrieves supported assets, markets and exchanges as per the API:
 * https://api.ae3platform.com/docs#tag/Reference
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
from apexe3.apexe3 import fetch_reference_data
from apexe3.apexe3 import fetch_exchanges_for_pair

from pandas.io.json import json_normalize
import pandas as pd


def init():
  clientId = "your-client-id-goes-here"
  clientSecret = "your-client-secret-goes-here"
  initialise(clientId, clientSecret)
  exchanges = fetch_exchanges_for_pair('eth', 'usdc')
  
  assets = fetch_reference_data("/reference/assets")
  supportedAssets = json_normalize(assets)
  print(supportedAssets)
  
  markets = fetch_reference_data("/reference/markets")
  supportedMarkets = json_normalize(markets)
  print(supportedMarkets)
  
  exchanges = fetch_reference_data("/reference/exchanges")
  supportedExchanges = json_normalize(exchanges)
  print(supportedExchanges)


      
if __name__ == "__main__":
    init()
  

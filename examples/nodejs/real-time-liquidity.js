/**
 * real-time-liquidity.js
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

const cTable = require('console.table');
const apexe3 = require('./apexe3/apexe3');

const clientId = "Your-ClientId-Goes-Here";
const clientSecret = "Your-Client-Secret-Goes-Here";

(async () => {

    const stream = await initGlobalOrderbook('BTC', 'USDT');

    stream.on('LIVE_LIQUIDITY', (globalLiquidity) => {

        console.table(['Exchange', 'Ask Liquidity', 'Bid Liquidity' , 'Asset Amount', 'Imbalance', 'Market Price_25'], globalLiquidity);

    });

    stream.on('LIVE_LIQUIDITY_STATS', (globalLiquidityStats) => {

        console.table(['Total Available Liquidity', 'Total Available Asset', 'Total Imbalance'], globalLiquidityStats);

    });

})();

async function initGlobalOrderbook(base, quote) {
    await apexe3.initialise(clientId, clientSecret);
    return await apexe3.initialiseGlobalOrderbook(base, quote, null, null);
}



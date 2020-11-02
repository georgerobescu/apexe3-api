/**
 * real-time-insights.js
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

const apexe3 = require('./apexe3/apexe3');

const clientId = "Your-ClientId-Goes-Here";
const clientSecret = "Your-Client-Secret-Goes-Here";

(async () => {

  const base = 'BTC';
  const quote = 'USD';
  const stream = await initInsightsForPair(base,quote);

  stream.on('VOI_BID', (message) => {
    console.log("BID VOIS for ", base, quote);
    console.table(message.values, [0,5]);
  });

  stream.on('WHALE', (message) => {
    console.log("WHALES for ", base, quote);
    console.table(message.values,[0,5]);

  });

  stream.on('VOI_ASK', (message) => {
    console.log("ASK VOIS for ", base, quote);
    console.table(message.values,[0,5]);
  });

  stream.on('SPREAD', (message) => {
    console.log("SPREADS for ", base, quote);
    console.table(message.values,[0,5]);
  });

  stream.on('ARBITRAGE', (message) => {
    console.log("ARBITRAGES For ", base, quote);
    console.table(message.values,[1,2,5]);
  });



})();

async function initInsightsForPair(base,quote) {

  await apexe3.initialise(clientId, clientSecret);
  return apexe3.initialiseDefaultInsightsForPair(base,quote);

}


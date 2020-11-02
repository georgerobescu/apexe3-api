/**
 * supported-assets-markets-exchanges.js
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
const apexe3 = require('./apexe3/apexe3');

(async () => {

    await init();

    const supportedAssets = await apexe3.fetchReferenceData('/reference/assets');
    console.table(supportedAssets);

    const supportedMarkets = await apexe3.fetchReferenceData('/reference/markets');
    console.table(supportedMarkets);

    const supportedExchanges = await apexe3.fetchReferenceData('/reference/exchanges');
    console.table(supportedExchanges);

})();


async function init() {

    const clientId = "Your-ClientId-Goes-Here";
    const clientSecret = "Your-Client-Secret-Goes-Here";
    
    await apexe3.initialise(clientId, clientSecret);

}
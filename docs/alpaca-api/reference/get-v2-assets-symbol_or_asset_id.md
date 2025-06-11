---
title: Get an Asset by ID or Symbol
source: reference\get-v2-assets-symbol_or_asset_id.html
---

get https://paper-api.alpaca.markets/v2/assets/{symbol_or_asset_id}
Get the asset model for a given symbol or asset_id. The symbol or asset_id should be passed in as a path parameter.
**Note** : For crypto, the symbol has to follow old symbology, e.g. BTCUSD.
**Note** : For coin pairs, the symbol should be separated by spare symbol (/), e.g. BTC/USDT. Since spare is a special character in HTTP, use the URL encoded version instead, e.g. /v2/assets/BTC%2FUSDT

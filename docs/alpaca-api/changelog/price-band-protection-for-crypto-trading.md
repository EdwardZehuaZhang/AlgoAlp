---
title: Price band protection for crypto trading
source: changelog\price-band-protection-for-crypto-trading.html
---

Price band protection introduced to prevent trades from executing outside a predefined percentage range around an external reference price.
**Order Validation Updates**  
Orders that would execute at an invalid price will be automatically canceled.
**Reject Reasons Updates**  
Orders may now be canceled with the following reasons:
1. canceled due to reference price stale – Order was canceled because the reference price used for price band validation was outdated.
2. canceled due to price band protection. Index price: <index_price> Price band: <price_band>%, Rejected price: <maker_order_price> – Order was about to execute at a price exceeding the allowed range

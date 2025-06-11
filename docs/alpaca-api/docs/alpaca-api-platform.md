---
title: Alpaca API Platform
source: docs.alpaca.markets\docs\alpaca-api-platform.html
---

# 
Why API?
Alpaca’s features to access financial markets are provided primarily via API. We believe API is the means to interact with services such as ours and innovate your business. Our API is designed to fit your needs and we continue to build what you need.
# 
REST, SSE and Websockets
Our API is primarily built in the REST style. It is a simple and powerful way to integrate with our services.
In addition to the REST API which replies via synchronous communication, our API includes an asynchronous event API which is based on WebSocket and SSE, or [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html). As many types of events occur in the financial markets (orders fill based on the market movement, cash settles after some time, etc), this event-based API helps you get updates instantly and provide the best user experiences to your customers.
# 
Architecture
Alpaca’s platform consists of APIs, Web dashboards, trade simulator, sandbox environment, authentication services, order management system, trading routing, back office accounting and clearing system, and all of these components are built in-house from the ground up with modern architecture.
The Alpaca platform is currently hosted on the Google Cloud Platform in the us-east4 region. The site is connected with dedicated fiber lines to a data center in Secaucus, NJ, to cross-connect with various market venues.
Under the hood, Alpaca works with various third parties. As we are self clearing for equities trade clearing and settlement on DTCC, we work with Velox Clearing for options trade clearing and settlement with the OCC. Cash transfers and custody are primarily provided by BMO Harris and Silicon Valley Bank and we use Currency Cloud and Airwallex for funding wallets and international transfers. Citadel Securities, Virtu America, Jane Street, Ion Group, and other execution providers provide execution services for our customer orders. We integrate with ICE Data Services for various kinds of market data. 
Alpaca Crypto executes customer trades on our internal central limit order book, self-clears all trades and does not custody customer cash but has banking relationships with Cross River Bank, Choice Financial and FVBank. To provide live market data, Alpaca Crypto works with Coinbase, Kraken, FalconX and Stillman Digital.
# 
API Updates & Upgrades
In an effort to continuously provide value to our developers, Alpaca frequently performs updates and upgrades to our API.
We’ve added the following sections to our docs in order to help make sure that as a developer you know what to expect, when to expect, and how to properly handle certain scenarios .
## 
Backwards Compatible Changes
You should expect any of the following kind of changes that we make to our API to be considered a backwards compatible change:
* Adding new or similarly named APIs
* Adding new fields to already defined models and objects such as API return objects, nested objects, etc. (Example: adding a new code field to error payloads)
* Adding new items to defined sets or enumerations such as statuses, supported assets, etc. (Example: adding new account status to a set of all )
* Enhancing ordering on how certain lists get returned
* Supporting new HTTP versions (HTTP2, QUIC)
* Adding new HTTP method(s) for an existing endpoint
* Expecting new HTTP request headers (eg. new authentication)
* Sending new HTTP headers (eg. HTTP caching headers, gzip encoding, etc.)
* Increasing HTTP limits (eg. Nginx large-client-header-buffers)
* Increasing rate limits
* Supporting additional SSL/TLS versions
Generally, as a rule of thumb, any append or addition operation is considered a backwards compatible update and does not need an upfront communication. These updates should be backwards compatible with existing interfaces and not cause any disruption to any clients calling our APIs.
## 
Breaking Changes
When and if Alpaca decides to perform breaking changes to our APIs the following should be expected:
* Upfront communication with sufficient time to allow developers to be able to react to new upcoming changes
* Our APIs are versioned, if breaking changes are intended we will generally bump the API version. For example, a route might go from being `/v1/accounts/{account_id}` to `/v2/accounts/{account_id}` if we had to make a breaking change to either the parameters it can take or its return structure
__Updated about 2 months ago
* * *

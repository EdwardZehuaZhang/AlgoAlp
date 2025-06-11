---
title: Getting Started with Trading API
source: docs\getting-started-with-trading-api.html
---

# 
Request ID
[](getting-started-with-trading-api.html#request-id)
All trading API endpoint provides a unique identifier of the API call in the response header with `X-Request-ID` key, the Request ID helps us to identify the call chain in our system. 
Make sure you provide the Request ID in all support requests that you created, it could help us to solve the issue as soon as possible. Request ID can't be queried in other endpoints, that is why we suggest to persist the recent Request IDs.
Shell
$ curl -v https://paper-api.alpaca.markets/v2/account
...
> GET /v2/account HTTP/1.1
> Host: paper-api.alpaca.markets
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Date: Fri, 25 Aug 2023 09:34:40 GMT
< Content-Type: application/json
< Content-Length: 26
< Connection: keep-alive
< X-Request-ID: 649c5a79da1ab9cb20742ffdada0a7bb
<
...
__Updated over 1 year ago
* * *

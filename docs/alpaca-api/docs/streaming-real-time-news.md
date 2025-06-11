---
title: Real-time News
source: docs\streaming-real-time-news.html
---

This API provides stock market news on a websocket stream. You can find the general description of the real-time WebSocket Stream [here](streaming-market-data.md). This page focuses on the news stream.
# 
URL
[](streaming-real-time-news.html#url)
The URL for the news stream is
wss://stream.data.alpaca.markets/v1beta1/news
Sandbox URL:
wss://stream.data.sandbox.alpaca.markets/v1beta1/news
# 
Channels
[](streaming-real-time-news.html#channels)
## 
News
[](streaming-real-time-news.html#news)
### 
Schema
[](streaming-real-time-news.html#schema)
Attribute| Type| Notes  
---|---|---  
T| string| Type of message (“n” for news)  
id| int| News article ID  
headline| string| Headline or title of the article  
summary| string| Summary text for article (may be first sentence of content)  
author| string| Original author of news article  
created_at| string| Date article was created in [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) format  
updated_at| string| Date article was updated in [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339) format  
content| string| Content of news article (might contain HTML)  
url| string| URL of article (if applicable)  
symbols| array| List of related or mentioned symbols  
source| string| Source where the news originated from (e.g. Benzinga)  
### 
Example
[](streaming-real-time-news.html#example)
JSON
{
"T": "n",
"id": 24918784,
"headline": "Corsair Reports Purchase Of Majority Ownership In iDisplay, No Terms Disclosed",
"summary": "Corsair Gaming, Inc. (NASDAQ:CRSR) (“Corsair”), a leading global provider and innovator of high-performance gear for gamers and content creators, today announced that it acquired a 51% stake in iDisplay",
"author": "Benzinga Newsdesk",
"created_at": "2022-01-05T22:00:37Z",
"updated_at": "2022-01-05T22:00:38Z",
"url": "https://www.benzinga.com/m-a/22/01/24918784/corsair-reports-purchase-of-majority-ownership-in-idisplay-no-terms-disclosed",
"content": "\u003cp\u003eCorsair Gaming, Inc. (NASDAQ:\u003ca class=\"ticker\" href=\"https://www.benzinga.com/stock/CRSR#NASDAQ\"\u003eCRSR\u003c/a\u003e) (\u0026ldquo;Corsair\u0026rdquo;), a leading global ...",
"symbols": ["CRSR"],
"source": "benzinga"
}
# 
Example
[](streaming-real-time-news.html#example-1)
JSON
$ websocat -H="APCA-API-KEY-ID: ${APCA_API_KEY_ID}" -H="APCA-API-SECRET-KEY: ${APCA_API_SECRET_KEY}" \
"${APCA_API_STREAM_URL}/v1beta1/news"
[{"T":"success","msg":"connected"}]
[{"T":"success","msg":"authenticated"}]
{"action":"subscribe","news":["*"]}
[{"T":"subscription","news":["*"]}]
[{"T":"n","id":40892639,"headline":"VinFast Officially Launches VF 3 Electric Vehicle In The Philippines","summary":"VinFast Auto has officially opened pre-orders for the VF 3 in the Philippines. From September 19 to 30, early customers who reserve the VF 3 will enjoy several attractive incentives and privileges, including a","author":"Benzinga Newsdesk","created_at":"2024-09-17T09:02:44Z","updated_at":"2024-09-17T09:02:45Z","url":"https://www.benzinga.com/news/24/09/40892639/vinfast-officially-launches-vf-3-electric-vehicle-in-the-philippines","content":"\u003cp\u003eVinFast Auto has officially opened pre-orders for the VF 3 in the Philippines.\u003c/p\u003e\u003cp\u003e\u0026nbsp;\u003c/p\u003e\u003cp\u003eFrom September 19 to 30, early customers who reserve the VF 3 will enjoy several attractive incentives and privileges, including a special price of 605,000 pesos (battery subscription) or 705,000 pesos (battery included). After this period, the prices will revert to the MSRP of 645,000 pesos (battery subscription) and 745,000 pesos (battery included).\u003cbr\u003e\u003cbr\u003eAdditionally, early VF 3 customers will have the privilege of choosing from nine striking exterior paint colors, including four base colors and five premium options, free of charge. Premium paint colors will cost an additional 20,000 pesos after this period.\u003cbr\u003e\u003cbr\u003eMoreover, from September 19 to 30, for only 40,000 pesos, early customers can customize their car's paint beyond the nine available colors. This will be the only time VinFast offers this exclusive privilege for the VF 3.\u003cbr\u003e\u003cbr\u003eVinFast is accepting deposits of 5,000 pesos through its official website or at authorized dealerships (refundable under VinFast's terms).\u003cbr\u003e\u0026nbsp;\u003c/p\u003e","symbols":["VFS"],"source":"benzinga"}]
__Updated 9 months ago
* * *

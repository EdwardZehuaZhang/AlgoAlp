---
title: Historical Stock Data
source: docs\historical-stock-data-1.html
---

This API provides historical market data for equities. Check the [API Reference](..-reference-stockbars-1.md) for the detailed descriptions of all the endpoints.
# 
Data Sources
[](historical-stock-data-1.html#data-sources)
Alpaca offers market data from two distinct data sources:
Source| Description  
---|---  
**IEX (Investors Exchange LLC)**|  IEX is ideal for initial app testing and situations where precise pricing may not be the primary focus. It accounts for approximately ~2.5% of the market volume.  
**SIP (All US Exchanges)**|  This Alpaca data feed originates directly from exchanges and is consolidated by the Securities Information Processors (SIPs). These SIPs play a crucial role in connecting various U.S. markets, processing and consolidating all bid/ask quotes and trades from multiple trading venues into a single, easily accessible data feed.  
Our data delivery ensures ultra-low latency and high reliability, as the information is transmitted directly to Alpaca's bare metal servers located in New Jersey, situated alongside many market participants.  
SIP data is particularly advantageous for developing your trading app, where precise and up-to-date price information is essential for traders and internal operations. It accounts for 100% of the market volume, providing comprehensive coverage for your trading needs.  
You can use the `feed` parameter on all the stock endpoints to switch between the data sources.
__Updated about 2 months ago
* * *

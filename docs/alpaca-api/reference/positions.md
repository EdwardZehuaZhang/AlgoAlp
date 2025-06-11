---
title: Positions
source: reference\positions.html
---

# 
Positions
[](positions.html#positions)
## 
Get All Open Positions For Account
[](positions.html#get-all-open-positions-for-account)
#### 
BrokerClient.get_all_positions_for_account(account_id: Union[UUID, str])
[](positions.html#brokerclientget_all_positions_for_accountaccount_id-unionuuid-str)
Gets all the current positions for an account.
* **Parameters:**  
**account_id** (_Union**[** UUID**,_ _str**]_) – The ID of the Account to get the open positions for.
* **Returns:**  
List of open positions from the account.
* **Return type:**  
List[[Position](https://docs.alpaca.markets/trading/models.md#alpaca.trading.models.Position)]
## 
Get A Open Position For Account
[](positions.html#get-a-open-position-for-account)
#### 
BrokerClient.get_open_position_for_account(account_id: Union[UUID, str], symbol_or_asset_id: Union[UUID, str])
[](positions.html#brokerclientget_open_position_for_accountaccount_id-unionuuid-str-symbol_or_asset_id-unionuuid-str)
Gets the open position for an account for a single asset. Throws an APIError if the position does not exist.
* **Parameters:**
* **account_id** (_Union**[** UUID**,_ _str**]_) – The ID of the Account to get the open position for.
* **symbol_or_asset_id** (_Union**[** UUID**,_ _str**]_) – The symbol name of asset id of the position to get from the account.
* **Returns:**  
Open position of the asset from the account.
* **Return type:**  
[Position](https://docs.alpaca.markets/trading/models.md#alpaca.trading.models.Position)
## 
Close All Positions For Account
[](positions.html#close-all-positions-for-account)
#### 
BrokerClient.close_all_positions_for_account(account_id: Union[UUID, str], cancel_orders: Optional[bool] = None)
[](positions.html#brokerclientclose_all_positions_for_accountaccount_id-unionuuid-str-cancel_orders-optionalbool--none)
Liquidates all positions for an account.
Places an order for each open position to liquidate.
* **Parameters:**
* **account_id** (_Union**[** UUID**,_ _str**]_) – The ID of the Account to close the positions for.
* **cancel_orders** (_Optional**[** bool**]_) – If true is specified, cancel all open orders before liquidating all positions.
* **Returns:**  
A list of responses from each closed position containing the status code and  
: order id.
* **Return type:**  
List[[ClosePositionResponse](https://docs.alpaca.markets/trading/models.md#alpaca.trading.models.ClosePositionResponse)]
## 
Close A Position For Account
[](positions.html#close-a-position-for-account)
#### 
BrokerClient.close_position_for_account(account_id: Union[UUID, str], symbol_or_asset_id: Union[UUID, str], close_options: Optional[[ClosePositionRequest](https://docs.alpaca.markets/trading/requests.md#alpaca.trading.requests.ClosePositionRequest)] = None)
[](positions.html#brokerclientclose_position_for_accountaccount_id-unionuuid-str-symbol_or_asset_id-unionuuid-str-close_options-optionalclosepositionrequest--none)
Liquidates the position for an account for a single asset.
Places a single order to close the position for the asset.
* **Parameters:**
* **account_id** (_Union**[** UUID**,_ _str**]_) – The ID of the Account to close the position for.
* **symbol_or_asset_id** (_Union**[** UUID**,_ _str**]_) – The symbol name of asset id of the position to close on the account.
* **close_options** – The various close position request parameters.
* **Returns:**  
The order that was placed to close the position.
* **Return type:**  
alpaca.broker.models.Order

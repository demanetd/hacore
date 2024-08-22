# ExchangeRateInformationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_currency** | **str** | Currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP &#x3D; xxxCUR, the unit currency is GBP.  | [optional] 
**exchange_rate** | **float** | The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.  | [optional] 
**rate_type** | **str** | Specifies the type used to complete the currency exchange. * Spot: Exchange rate applied is the spot rate. * Sale: Exchange rate applied is the market rate at the time of the sale. * Agreed: Exchange rate applied is the rate agreed between the parties.  | [optional] 
**contract_identification** | **str** | Unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent.  | [optional] 
**expiration_date_time** | **datetime** | Expiration date time. ISO 8601 DateTime.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


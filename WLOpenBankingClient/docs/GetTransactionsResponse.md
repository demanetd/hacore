# GetTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** | Date and time. All transactions on this date are included in the result.  | [optional] 
**date_to** | **datetime** | Date and time, transactions up to this date are included. So transaction on this date are not included in the result.  | [optional] 
**account_id** | **str** | Id of the account of the PSU as retrieved form the GET accounts response.  | 
**transactions** | [**list[Transactions]**](Transactions.md) |  | [optional] 
**links** | [**TransactionLinks**](TransactionLinks.md) |  | [optional] 
**metadata** | [**Meta**](Meta.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


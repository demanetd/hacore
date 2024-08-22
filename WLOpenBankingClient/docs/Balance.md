# Balance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_name** | **str** | Label of the balance.  | [optional] 
**amount** | [**Amount**](Amount.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**balance_type** | [**BalanceType**](BalanceType.md) |  | 
**credit_debit_indicator** | [**CreditDebitIndicator**](CreditDebitIndicator.md) |  | 
**last_commited_transaction** | **str** | entryReference of the last committed transaction to support the Initiating Party in identifying whether all PSU transactions are already known.  | [optional] 
**credit_line** | [**list[CreditLine]**](CreditLine.md) |  | [optional] 
**_date** | **str** | Indicates the date of the balance. Date in ISO 8601 format yyyy -MM-dd.  | [optional] 
**last_change_date_time** | **datetime** | Timestamp of the last change of the balance amount. This data element might be used to indicate e.g. with the expected or booked balance that no action is known on the account, which is not yet booked.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


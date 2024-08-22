# PeriodRules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **datetime** | Date of first occurence. ISO 8601 DateTime.  | 
**execution_rule** | **str** | Specifies the execution rule to follow in the cases when the computed execution dates cannot be processed (e.g. bank holidays). The default value sent to the ASPSP will be FWNG.  | [optional] 
**end_date** | **str** | Optional date for closing the periodic payment. Must be given in ISO LOCAL DATE format.  | [optional] 
**frequency** | **str** | Specifies the frequency of the payment in order to compute further execution dates.  | 
**day_of_execution** | **int** | Sepcifies the day of execution. Day of the month 1...31. Applicable only for MNTH or higher.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# ConsentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psu_data** | [**PsuData**](PsuData.md) |  | [optional] 
**use_pre_authentication** | **bool** | This field is only applicable for ASPSP&#x27;s which support pre-authentication. It can also be filled in consent requests toward other ASPSP&#x27;s, but the value will then be ignored.  * If set to true the Open Banking Service will store the pre-authentication token for use with future consent requests. This will only work if also a PsuId is provided which is stored in the Open Banking Service. &lt;br&gt;  * If set to false the pre-authentication token will only be used to finish one consent request. After which it will be discarded.  | [optional] [default to False]
**preferred_sca_method** | **list[str]** |  | [optional] 
**permissions** | [**list[PermissionEnum]**](PermissionEnum.md) |  | [optional] 
**details** | [**ConsentDetails**](ConsentDetails.md) |  | [optional] 
**transaction_from_date_time** | **datetime** | Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction. | [optional] 
**transaction_to_date_time** | **datetime** | Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# ConsentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permitted_account_references** | [**list[PermittedAccountReference]**](PermittedAccountReference.md) |  | [optional] 
**valid_until_date** | **date** | This parameter is requesting a valid until date for the requested consent. If this date is not given in the request a validity period of 90 days is used towards the ASPSP.  | [optional] 
**frequency_per_day** | **int** | This field indicates the requested maximum frequency for an access per day. Allowed unattended requests per day 1-4.  | [optional] 
**recurring_indicator** | **bool** | Indicates if the consent is for recurring access or for one time access to the account data.  **Note -** Default value is set to false, only for ASPSPs having implemented the CBI protocol.  | [optional] 
**combined_service_indicator** | **bool** | If \&quot;true\&quot; indicates that a payment initiation service will be addressed in the same \&quot;session\&quot;.  | [optional] [default to False]
**owner_name** | **bool** | If true the Open Banking Service will ask the ASPSP for the Owername of the accounts.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


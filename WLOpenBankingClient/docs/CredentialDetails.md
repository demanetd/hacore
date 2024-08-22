# CredentialDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_secret** | **str** | Binary identification of the transparancy of the provided credentials by the PSU. Can have 2 values, * true * false  Can be provided by ASPSP. If not provided by the ASPSP then by default, * true, if the CredentialId&#x3D;ewl-password * false, if CredentialId&#x3D;ewl-user-id  | 
**credential_id** | **str** | Credential detail identification of the PSU credential at the bank (provided by CBI if approach is Embedded). If not provided by the ASPSP, then default values should be, * ewl-user-id, when IsSecret&#x3D;false * ewl-password, when IsSecret&#x3D;true  | [optional] 
**label_list** | [**list[CredentialLabel]**](CredentialLabel.md) | The list of the labels to show to the PSU. They are internationalized.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


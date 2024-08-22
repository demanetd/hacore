# ConsentAuthorisationUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psu_data** | [**PsuDataIdentification**](PsuDataIdentification.md) |  | [optional] 
**psu_credentials** | [**list[PsuAuthCredentials]**](PsuAuthCredentials.md) | List of PSU&#x27;s credentials.  | [optional] 
**authentication_method_id** | **str** | Id of the selected method.  | [optional] 
**sca_authentication_data** | **str** | Depending on method. In case of binary data it has to be given base64 encoded.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


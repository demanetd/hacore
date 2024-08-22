# AuthorisationRequiredData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psu_credentials** | [**list[PsuCredentials]**](PsuCredentials.md) | List of credentials the PSU has on the ASPSP&#x27;s system. The PSU has to provide the CredentialValue for each of these (Username &amp; Password).  | [optional] 
**sca_methods** | [**list[ScaMethods]**](ScaMethods.md) | Array of available ScaMethods.  | [optional] 
**chosen_sca_method** | [**ScaMethods**](ScaMethods.md) |  | [optional] 
**challenge_data** | [**ScaChallengeData**](ScaChallengeData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


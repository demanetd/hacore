# CommonPaymentDataRefund

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiating_party_reference_id** | **str** | Reference to the payment created by the Initiating Party. This Id will not be visible to the Payment Service User.  | 
**use_pre_authentication** | **bool** | Whether or not the pre-authentication token should be re-used.  | [optional] [default to False]
**preferred_sca_method** | **list[str]** |  | [optional] 
**psu_data** | [**PsuData**](PsuData.md) |  | [optional] 
**refunds** | [**list[Refund]**](Refund.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


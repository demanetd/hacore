# PaymentInitiationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_product** | [**list[PaymentProductEnum]**](PaymentProductEnum.md) | Multiple PaymentProducts can only be supplied if &#x60;UseAuthorisationLandingPages&#x60; equals &#x60;TRUE&#x60;. These will then influence ASPSPs visible to the PSU on the Bank Selection Interface. The IDEAL payment product cannot be mixed with the other PSD2-xxxx payment products, because it requires a separate subscription and therefore uses a different authorization token.  | [optional] 
**payment_product_changeable** | **bool** | Allowing PSU to change pre-selected payment product if the ASPSP supports more than one from the list provided by the Initiating Party. Usable only if &#x60;UseAuthorisationLandingPages&#x60; equals &#x60;TRUE&#x60;. Otherwise will be ignored.  | [optional] [default to False]
**product_specific_master_data** | [**list[ProductSpecificMasterData]**](ProductSpecificMasterData.md) | The array is defined to mention the master data specific to selected payment product  | [optional] 
**psu_data** | [**PsuData**](PsuData.md) |  | [optional] 
**common_payment_data** | [**PaymentInitiationRequestBasic**](PaymentInitiationRequestBasic.md) |  | 
**ideal_payments** | [**IDEALPayments**](IDEALPayments.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


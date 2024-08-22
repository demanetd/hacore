# RiskInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_context_code** | **str** | Specifies the payment context. Payments for EcommerceGoods and EcommerceServices will be expected to have a MerchantCategoryCode and MerchantCustomerIdentification populated. Payments for EcommerceGoods will also have the DeliveryAddress populated.  | [optional] 
**merchant_category_code** | **str** | Category code conform to ISO 18245, related to the type of services or goods the merchant provides for the transaction.  | [optional] 
**merchant_customer_id** | **str** | The unique customer identifier of the PSU with the merchant.  | [optional] 
**delivery_address** | **AllOfRiskInformationDeliveryAddress** | The Object is deprecated and will be ignored in the current implementation. Use &#x60;DebtorInformation.ShippingAddress&#x60; from &#x60;CommonPaymentData&#x60; object instead  | [optional] 
**channel_type** | **str** | Payment channel type.  | [optional] 
**channel_meta_data** | **str** | Additional information related to the channel.  | [optional] 
**applied_authentication_approach** | **str** | Indicates the Applied Authentication Approach  | [optional] 
**reference_payment_order_id** | **str** | Indicates the Applied Authentication Approach  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


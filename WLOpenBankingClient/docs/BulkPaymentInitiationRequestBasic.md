# BulkPaymentInitiationRequestBasic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_pre_authentication** | **bool** | This field is only applicable for ASPSP&#x27;s which support pre-authentication. It can also be filled in payments toward other ASPSP&#x27;s, but the value will then be ignored. * If set to true the Open Banking Service will store the pre-authentication token for use with future payments. This will only work if also a PsuId is provided which is stored in the Open Banking Service. * If set to false the pre-authentication token will only be used to finish one payment. After which it will be discarded.  | [optional] [default to False]
**initiating_party_reference_id** | **str** | Reference to the payment created by the Initiating Party. This Id will not be visible to the Payment Service User. Required for PSD2 payments  | [optional] 
**preferred_sca_method** | **list[str]** | Multiple preferred methods can be choosen. It is not guaranteed that the ASPSP will use the preferred method.  | [optional] 
**transaction_type** | **str** | Transaction type used in this transaction. ONLINE - Used particularly for Online transactions, e.g. a webshop QR - Used for transactions from a QR. eg. Invoice INSTORE - Used for instore transactions for eg.- a POS device P2P - Used for peer-to-peer (customer-to-customer) transactions, e.g. a Transaction Request  | [optional] [default to 'Online']
**expiration_period** | **int** | Time in seconds after which the transaction will expire. If not provided a default value will be used if the &#x60;PaymentProduct&#x60; equals &#x60;IDEAL&#x60;. For ONLINE - 1200 and for INSTORE - 120. Required for QR type transactions  | [optional] 
**debtor_information** | [**DebtorInformation**](DebtorInformation.md) |  | [optional] 
**charge_bearer** | **str** | Charge bearer.  Note - ISO20022 ChargeBearerType1Code.  | [optional] 
**category_purpose** | [**CategoryPurposeEnum**](CategoryPurposeEnum.md) |  | [optional] 
**payment_context** | [**RiskInformation**](RiskInformation.md) |  | [optional] 
**payments** | [**list[BulkPaymentsDetails]**](BulkPaymentsDetails.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


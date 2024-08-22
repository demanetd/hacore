# PaymentInitiationRequestBasic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_pre_authentication** | **bool** | This field is only applicable for Aspsp which support pre-authentication. It can also be filled in payments toward other ASPSP&#x27;s, but the value will then be ignored. * If set to true the Open Banking Service will store the pre-authentication token for use with future payments. This will only work if also a PsuId is provided which is stored in the Open Banking Service. * If set to false the pre-authentication token will only be used to finish one payment. After which it will be discarded.  | [optional] [default to False]
**end_to_end_id** | **str** | Unique identification, as assigned by the initiating party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the transaction. It can be included in several messages related to the transaction. Required for PSD2 payments  | [optional] 
**initiating_party_reference_id** | **str** | Reference to the payment created by the Initiating Party. This Id will not be visible to the Payment Service User. Required for PSD2 payments  | [optional] 
**preferred_sca_method** | **list[str]** | Multiple preferred methods can be choosen. It is not guaranteed that the ASPSP will use the preferred method.  | [optional] 
**transaction_type** | **str** | Transaction type used in this transaction. ONLINE - Used particularly for Online transactions, e.g. a webshop QR - Used for transactions from a QR. eg. Invoice INSTORE - Used for instore transactions for eg.- a POS device P2P - Used for peer-to-peer (customer-to-customer) transactions, e.g. a Transaction Request  | [optional] [default to 'Online']
**expiration_period** | **int** | Time in seconds after which the transaction will expire. If not provided a default value will be used if the &#x60;PaymentProduct&#x60; equals &#x60;IDEAL&#x60;. For ONLINE - 1200 and for INSTORE - 120. Required for QR type transactions  | [optional] 
**amount** | [**Amount**](Amount.md) |  | 
**debtor_information** | [**DebtorInformation**](DebtorInformation.md) |  | [optional] 
**creditor_information** | [**CreditorInformation**](CreditorInformation.md) |  | [optional] 
**charge_bearer** | **str** | Charge bearer.  Note - ISO20022 ChargeBearerType1Code.  | [optional] 
**purpose_code** | **str** | Specifies the purpose code that resulted in a payment initiation. Fill with a 4 characters code from the ExternalPurpose1Code list published by ISO20022 or use the values ‘Commerce’, ‘Carpark’, ‘Transport’.  | [optional] 
**category_purpose** | [**CategoryPurposeEnum**](CategoryPurposeEnum.md) |  | [optional] 
**payment_context** | [**RiskInformation**](RiskInformation.md) |  | [optional] 
**cross_currency_payments** | [**CrossCurrencyPayment**](CrossCurrencyPayment.md) |  | [optional] 
**regulatory_reporting_codes** | [**list[RegulatoryReportingCode]**](RegulatoryReportingCode.md) | List of needed regulatory reporting codes for international payments  | [optional] 
**remittance_information** | **str** | Information supplied to enable the matching of an entry with the items that the transfer is intended to settle. This information will be visible to the Payment Service User.  **Conditional validation:** * In case the PaymentProduct is set to IDEAL the maxLength is limited to 35  | [optional] 
**remittance_information_structured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


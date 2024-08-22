# BulkPaymentsDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_to_end_id** | **str** | Unique identification, as assigned by the Initiating Party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the transaction. It can be included in several messages related to the transaction. Required for PSD2 payments  | 
**amount** | [**Amount**](Amount.md) |  | 
**creditor_information** | [**CreditorInformation**](CreditorInformation.md) |  | [optional] 
**purpose_code** | **str** | Specifies the purpose code that resulted in a payment initiation. Fill with a 4 characters code from the ExternalPurpose1Code list published by ISO20022 or use the values ‘Commerce’, ‘Carpark’, ‘Transport’.  | [optional] 
**cross_currency_payments** | [**CrossCurrencyPayment**](CrossCurrencyPayment.md) |  | [optional] 
**regulatory_reporting_codes** | [**list[RegulatoryReportingCode]**](RegulatoryReportingCode.md) | List of needed regulatory reporting codes for international payments  | [optional] 
**remittance_information** | **str** | Information supplied to enable the matching of an entry with the items that the transfer is intended to settle. This information will be visible to the Payment Service User.  **Conditional validation:** * In case the PaymentProduct is set to IDEAL the maxLength is limited to 35  | [optional] 
**remittance_information_structured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


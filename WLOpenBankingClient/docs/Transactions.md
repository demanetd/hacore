# Transactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique identification, as assigned by the first instructing agent, to unambiguously identify the transaction that is passed on, unchanged, throughout the entire interbank chain. Not provided by all ASPSPs.  The transaction identification can be used for reconciliation, tracking or to link tasks relating to the transaction on the interbank level.  | [optional] 
**amount** | [**Amount**](Amount.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**credit_debit_indicator** | [**CreditDebitIndicator**](CreditDebitIndicator.md) |  | 
**status** | **str** | Type of transaction.  | 
**booking_date_time** | **datetime** | Booking date of the transaction on the account.  | 
**execution_date_time** | **datetime** | PSU Account transaction execution date.  | [optional] 
**value_date_time** | **datetime** | Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit entry.  | [optional] 
**transaction_date** | **str** | Indicates the date of the transaction. Date in ISO format yyyy -MM-dd.  | [optional] 
**remittance_information_unstructured** | **str** | Unstructured remittance information.  | [optional] 
**address_line** | **str** | Information that locates and identifies a specific address, as defined by postal services, that is presented in free format text.  | [optional] 
**bank_transaction_code** | [**BankTransactionCode**](BankTransactionCode.md) |  | [optional] 
**merchant_detail** | [**MerchantDetail**](MerchantDetail.md) |  | [optional] 
**creditor_agent** | [**CreditorAgent**](CreditorAgent.md) |  | [optional] 
**creditor_account** | [**CreditorAccount**](CreditorAccount.md) |  | [optional] 
**debtor_agent** | [**DebtorAgent**](DebtorAgent.md) |  | [optional] 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 
**purpose_code** | **str** | Specifies the external purpose code in the format of character string with a maximum length of 4 characters.  ISO 20022 ExternalPurpose1Code.  | [optional] 
**remittance_information_structured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  | [optional] 
**equivalent_amount** | [**EquivalentAmount**](EquivalentAmount.md) |  | [optional] 
**references** | [**References**](References.md) |  | [optional] 
**related_parties** | [**RelatedParties**](RelatedParties.md) |  | [optional] 
**currency_exchange** | [**list[CurrencyExchange]**](CurrencyExchange.md) | Set of elements used to provide details on the currency exchange.  | [optional] 
**category_id** | **str** | Identification of the category associated with the transaction. This field is reserved for future use and will only be filled if an extended service is contracted.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


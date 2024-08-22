# References

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_to_end_id** | **str** | Unique identification, as assigned by the Initiating Party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to end chain . Usage The end-to-end identification can be used for reconciliation or to link tasks relating to the transaction. It can be included in several messages related to the transaction.  | [optional] 
**mandate_id** | **str** | Identification of Mandates, e.g. a SEPA Mandate ID.  | [optional] 
**cheque_number** | **str** | Identification of a Cheque.  | [optional] 
**statement_reference** | **list[str]** | Can contains many statementReferences for OB UK.  | [optional] 
**transaction_reference** | **str** | Unique reference for the transaction. This reference is optionally populated, and may as an example be the FPID in the Faster Payments context.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


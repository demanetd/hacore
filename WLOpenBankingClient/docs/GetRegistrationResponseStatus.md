# GetRegistrationResponseStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | [**ProductType**](ProductType.md) |  | 
**registration_status** | [**RegistrationStatusEnum**](RegistrationStatusEnum.md) |  | [optional] 
**use_case_status** | **str** | Status indicating the progress of processing in the Open Banking platform for a given use case.    Credit Scoring:   - REGISTRATION_CREATED : A registration is created, waiting for consent sessions to be finalized.   - REGISTRATION_FINALISED : All PSUs in the registrations have completed their consent flow, data collection will start.   - DATA_COLLECTION_DONE : AIS data has been retrieved for all PSUs in the registration and has been sent for processing.   - DATA_COLLECTION_ERROR : An error happened during the data collection, the processing will not happen.   - ANALYSIS_FINALISED : The Credit Insight processing module has given feedback regarding the processing, report results will / have been sent to the InitiatingParty endpoint.  | [optional] 
**parameter** | [**Parameter**](Parameter.md) |  | [optional] 
**psus** | [**list[GetRegistrationResponseStatusPsus]**](GetRegistrationResponseStatusPsus.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# ASPSP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspsp_id** | **str** | Id of the ASPSP used within the Open Banking Service, to be used in other API’s to identify the ASPSP | 
**name** | [**list[NameLabel]**](NameLabel.md) |  | 
**bic** | **str** | BIC of the ASPSP | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**category_label** | **list[str]** |  | [optional] 
**details** | [**list[DetailsType]**](DetailsType.md) | This block only shows when query parameter allDetails &#x3D; true | [optional] 
**options** | [**list[OptionType]**](OptionType.md) | List of directory service options for the given ASPSP | [optional] 
**group_id** | **str** | An id referencing a group this ASPSP is part of. | [optional] 
**aspsp_specific_labels** | [**list[AspspSpecificLabel]**](AspspSpecificLabel.md) | List of Specific Labels for the given ASPSP | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


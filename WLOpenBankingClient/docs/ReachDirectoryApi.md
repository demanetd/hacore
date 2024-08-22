# swagger_client.ReachDirectoryApi

All URIs are relative to *https://xs2a.awltest.de/xs2a/routingservice/services/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reach**](ReachDirectoryApi.md#reach) | **GET** /directory/v3/aspsps | Get list of ASPSPs reachable with our Open Banking Services

# **reach**
> ReachDirectoryResponse reach(x_request_id, message_create_date_time, service, country=country, all_details=all_details, all_options=all_options, category_label=category_label, all_aspsp_specific_fields=all_aspsp_specific_fields)

Get list of ASPSPs reachable with our Open Banking Services

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ReachDirectoryApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
service = 'service_example' # str | The name of the service for which the reach will be retrieved. Only AIS or PIS is allowed. 
country = 'country_example' # str | List ASPSPs of given country only. ISO 3166-1, Alpha-2 standard  (optional)
all_details = false # bool | When `true` the details block in the response is provided.  (optional) (default to false)
all_options = false # bool | When `true` the options block in the response is provided.  (optional) (default to false)
category_label = 'category_label_example' # str | Filter request that contains a specified Label  (optional)
all_aspsp_specific_fields = false # bool | When `true` the AspspSpecificFields block in the response is provided.  (optional) (default to false)

try:
    # Get list of ASPSPs reachable with our Open Banking Services
    api_response = api_instance.reach(x_request_id, message_create_date_time, service, country=country, all_details=all_details, all_options=all_options, category_label=category_label, all_aspsp_specific_fields=all_aspsp_specific_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReachDirectoryApi->reach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **service** | **str**| The name of the service for which the reach will be retrieved. Only AIS or PIS is allowed.  | 
 **country** | **str**| List ASPSPs of given country only. ISO 3166-1, Alpha-2 standard  | [optional] 
 **all_details** | **bool**| When &#x60;true&#x60; the details block in the response is provided.  | [optional] [default to false]
 **all_options** | **bool**| When &#x60;true&#x60; the options block in the response is provided.  | [optional] [default to false]
 **category_label** | **str**| Filter request that contains a specified Label  | [optional] 
 **all_aspsp_specific_fields** | **bool**| When &#x60;true&#x60; the AspspSpecificFields block in the response is provided.  | [optional] [default to false]

### Return type

[**ReachDirectoryResponse**](ReachDirectoryResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


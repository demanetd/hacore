# swagger_client.DebtorPreferenceRetrievalApi

All URIs are relative to *https://xs2a.awltest.de/xs2a/routingservice/services/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_psu_banks_with_accounts**](DebtorPreferenceRetrievalApi.md#get_all_psu_banks_with_accounts) | **GET** /ob/pis/v3/preferences/{Psuid}/ | Get PSU preferred bank and preferred account

# **get_all_psu_banks_with_accounts**
> PsuBankPreferences get_all_psu_banks_with_accounts(psuid, x_request_id, message_create_date_time, aspsp_id, signature=signature, digest=digest, initiating_party_sub_id=initiating_party_sub_id)

Get PSU preferred bank and preferred account

Currently could be used only for iDEAL 2.0 payments 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DebtorPreferenceRetrievalApi(swagger_client.ApiClient(configuration))
psuid = 'psuid_example' # str | The Id of the PSU registered at the Open Banking Service 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
aspsp_id = 'aspsp_id_example' # str | ASPSP ID. 
signature = 'signature_example' # str | Conditionally required for iDEAL payments. The signature in the request should include a keyId with the value of fingerprint of the certificate  (optional)
digest = 'digest_example' # str | Is contained if and only if the `Signature` element is contained in the header of the request. (optional)
initiating_party_sub_id = 'initiating_party_sub_id_example' # str | External identification of the subsidiary initiating party.  (optional)

try:
    # Get PSU preferred bank and preferred account
    api_response = api_instance.get_all_psu_banks_with_accounts(psuid, x_request_id, message_create_date_time, aspsp_id, signature=signature, digest=digest, initiating_party_sub_id=initiating_party_sub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebtorPreferenceRetrievalApi->get_all_psu_banks_with_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psuid** | **str**| The Id of the PSU registered at the Open Banking Service  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **aspsp_id** | **str**| ASPSP ID.  | 
 **signature** | **str**| Conditionally required for iDEAL payments. The signature in the request should include a keyId with the value of fingerprint of the certificate  | [optional] 
 **digest** | **str**| Is contained if and only if the &#x60;Signature&#x60; element is contained in the header of the request. | [optional] 
 **initiating_party_sub_id** | **str**| External identification of the subsidiary initiating party.  | [optional] 

### Return type

[**PsuBankPreferences**](PsuBankPreferences.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


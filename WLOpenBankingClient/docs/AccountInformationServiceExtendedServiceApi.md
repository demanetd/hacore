# swagger_client.AccountInformationServiceExtendedServiceApi

All URIs are relative to *https://xs2a.awltest.de/xs2a/routingservice/services/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_registration**](AccountInformationServiceExtendedServiceApi.md#delete_registration) | **DELETE** /ob/ais/v3/register/{registrationId} | Delete an existing registration
[**get_registration_status**](AccountInformationServiceExtendedServiceApi.md#get_registration_status) | **GET** /ob/ais/v3/register/{registrationId}/status | Get an existing registration status
[**post_consent_authorisation**](AccountInformationServiceExtendedServiceApi.md#post_consent_authorisation) | **POST** /ob/ais/v3/register/{registrationId}/initialisation/{psuId} | Get the link to the IS for the consent authorisation
[**put_registration**](AccountInformationServiceExtendedServiceApi.md#put_registration) | **PUT** /ob/ais/v3/register/{registrationId} | Update an existing registration for the PSU
[**registration**](AccountInformationServiceExtendedServiceApi.md#registration) | **POST** /ob/ais/v3/register | POST a new registration resource for a specific product.

# **delete_registration**
> delete_registration(x_request_id, message_create_date_time, registration_id)

Delete an existing registration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
registration_id = 'registration_id_example' # str | Registration ID is the source ID, which is being created to link the PSUs under the same ProductType 

try:
    # Delete an existing registration
    api_instance.delete_registration(x_request_id, message_create_date_time, registration_id)
except ApiException as e:
    print("Exception when calling AccountInformationServiceExtendedServiceApi->delete_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **registration_id** | **str**| Registration ID is the source ID, which is being created to link the PSUs under the same ProductType  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_status**
> GetRegistrationResponseStatus get_registration_status(x_request_id, message_create_date_time, registration_id)

Get an existing registration status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
registration_id = 'registration_id_example' # str | Registration ID is the source ID, which is being created to link the PSUs under the same ProductType 

try:
    # Get an existing registration status
    api_response = api_instance.get_registration_status(x_request_id, message_create_date_time, registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceExtendedServiceApi->get_registration_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **registration_id** | **str**| Registration ID is the source ID, which is being created to link the PSUs under the same ProductType  | 

### Return type

[**GetRegistrationResponseStatus**](GetRegistrationResponseStatus.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_consent_authorisation**
> InitialisationResponse post_consent_authorisation(x_request_id, message_create_date_time, registration_id, psu_id, body=body, locale=locale, initiating_party_return_url=initiating_party_return_url)

Get the link to the IS for the consent authorisation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
registration_id = 'registration_id_example' # str | Registration ID is the source ID, which is being created to link the PSUs under the same ProductType 
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
body = swagger_client.InitialisationRequest() # InitialisationRequest |  (optional)
locale = 'locale_example' # str | 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  (optional)
initiating_party_return_url = 'initiating_party_return_url_example' # str | The callback URL for the redirection back to the Initiating Party after authorization.  (optional)

try:
    # Get the link to the IS for the consent authorisation
    api_response = api_instance.post_consent_authorisation(x_request_id, message_create_date_time, registration_id, psu_id, body=body, locale=locale, initiating_party_return_url=initiating_party_return_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceExtendedServiceApi->post_consent_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **registration_id** | **str**| Registration ID is the source ID, which is being created to link the PSUs under the same ProductType  | 
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **body** | [**InitialisationRequest**](InitialisationRequest.md)|  | [optional] 
 **locale** | **str**| 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  | [optional] 
 **initiating_party_return_url** | **str**| The callback URL for the redirection back to the Initiating Party after authorization.  | [optional] 

### Return type

[**InitialisationResponse**](InitialisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_registration**
> put_registration(x_request_id, message_create_date_time, registration_id, body=body)

Update an existing registration for the PSU

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
registration_id = 'registration_id_example' # str | Registration ID is the source ID, which is being created to link the PSUs under the same ProductType 
body = swagger_client.PutRegistrationRequest() # PutRegistrationRequest |  (optional)

try:
    # Update an existing registration for the PSU
    api_instance.put_registration(x_request_id, message_create_date_time, registration_id, body=body)
except ApiException as e:
    print("Exception when calling AccountInformationServiceExtendedServiceApi->put_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **registration_id** | **str**| Registration ID is the source ID, which is being created to link the PSUs under the same ProductType  | 
 **body** | [**PutRegistrationRequest**](PutRegistrationRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration**
> PostRegistrationResponse registration(x_request_id, message_create_date_time, body=body)

POST a new registration resource for a specific product.

The available products utilize the PSUs AIS consent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
body = swagger_client.PostRegistrationRequest() # PostRegistrationRequest |  (optional)

try:
    # POST a new registration resource for a specific product.
    api_response = api_instance.registration(x_request_id, message_create_date_time, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceExtendedServiceApi->registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **body** | [**PostRegistrationRequest**](PostRegistrationRequest.md)|  | [optional] 

### Return type

[**PostRegistrationResponse**](PostRegistrationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


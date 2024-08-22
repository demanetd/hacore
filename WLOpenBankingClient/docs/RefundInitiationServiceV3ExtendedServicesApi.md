# swagger_client.RefundInitiationServiceV3ExtendedServicesApi

All URIs are relative to *https://xs2a.awltest.de/xs2a/routingservice/services/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refund_authorisation**](RefundInitiationServiceV3ExtendedServicesApi.md#refund_authorisation) | **POST** /ob/pis/v3/refunds/{refundId}/authorisations | Refund authorisation request
[**refund_authorisation_update**](RefundInitiationServiceV3ExtendedServicesApi.md#refund_authorisation_update) | **PUT** /ob/pis/v3/refunds/{refundId}/authorisations/{authorisationId} | Refund authorisation request
[**refund_confirmation**](RefundInitiationServiceV3ExtendedServicesApi.md#refund_confirmation) | **POST** /ob/pis/v3/refunds/{refundId}/confirmation | Confirmation of the refund request by the PISP
[**refund_identification**](RefundInitiationServiceV3ExtendedServicesApi.md#refund_identification) | **POST** /ob/pis/v3/refunds/{refundId}/identification | Refund identification request
[**refund_initiate**](RefundInitiationServiceV3ExtendedServicesApi.md#refund_initiate) | **POST** /ob/pis/v3/refunds | Refund initiation request
[**refund_status**](RefundInitiationServiceV3ExtendedServicesApi.md#refund_status) | **GET** /ob/pis/v3/refunds/{refundId}/status | Status of the refund

# **refund_authorisation**
> RefundAuthorisationResponse refund_authorisation(x_request_id, message_create_date_time, refund_id, body=body)

Refund authorisation request

Use this operation to authorise a refund explicitly. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RefundInitiationServiceV3ExtendedServicesApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
refund_id = 'refund_id_example' # str | The Id used by the Open Banking Service to refer to a refund. 
body = swagger_client.PaymentAuthorisationRequest() # PaymentAuthorisationRequest | Description of request.
 (optional)

try:
    # Refund authorisation request
    api_response = api_instance.refund_authorisation(x_request_id, message_create_date_time, refund_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundInitiationServiceV3ExtendedServicesApi->refund_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **refund_id** | **str**| The Id used by the Open Banking Service to refer to a refund.  | 
 **body** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)| Description of request.
 | [optional] 

### Return type

[**RefundAuthorisationResponse**](RefundAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_authorisation_update**
> RefundAuthorisationResponse refund_authorisation_update(x_request_id, message_create_date_time, refund_id, authorisation_id, body=body)

Refund authorisation request

Use this operation to change the authorisation resource. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RefundInitiationServiceV3ExtendedServicesApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
refund_id = 'refund_id_example' # str | The Id used by the Open Banking Service to refer to a refund. 
authorisation_id = 'authorisation_id_example' # str | The Id used by the Open Banking Service to refer to an authorisation resource. 
body = swagger_client.PaymentAuthorisationUpdateRequest() # PaymentAuthorisationUpdateRequest |  (optional)

try:
    # Refund authorisation request
    api_response = api_instance.refund_authorisation_update(x_request_id, message_create_date_time, refund_id, authorisation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundInitiationServiceV3ExtendedServicesApi->refund_authorisation_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **refund_id** | **str**| The Id used by the Open Banking Service to refer to a refund.  | 
 **authorisation_id** | **str**| The Id used by the Open Banking Service to refer to an authorisation resource.  | 
 **body** | [**PaymentAuthorisationUpdateRequest**](PaymentAuthorisationUpdateRequest.md)|  | [optional] 

### Return type

[**RefundAuthorisationResponse**](RefundAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_confirmation**
> RefundConfirmationResponse refund_confirmation(x_request_id, message_create_date_time, refund_id, body=body, initiating_party_return_url=initiating_party_return_url, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location)

Confirmation of the refund request by the PISP

This API is used to confirm a refund, confirmation is required when the link 'ConfirmationRequired' is returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RefundInitiationServiceV3ExtendedServicesApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
refund_id = 'refund_id_example' # str | The Id used by the Open Banking Service to refer to a refund. 
body = swagger_client.ConfirmationRequest() # ConfirmationRequest |  (optional)
initiating_party_return_url = 'initiating_party_return_url_example' # str | The callback URL for the redirection back to the Initiating Party after authorization.  (optional)
last_login = '2013-10-20T19:20:30+01:00' # datetime | PSU Session information.  The time when the PSU last logged in with the TPP.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | PSU Session information.  The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
http_method = 'http_method_example' # str | PSU Session information.  HTTP method used at the PSU-TPP interface. Available values - GET, POST, PUT, DELETE.  (optional)
http_header_user_agent = 'http_header_user_agent_example' # str | PSU Session information.  The forwarded Agent header field of the HTTP request between PSU and TPP.  (optional)
http_header_referer = 'http_header_referer_example' # str | PSU Session information.  (optional)
http_header_accept = 'http_header_accept_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
http_header_accept_charset = 'http_header_accept_charset_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
http_header_accept_encoding = 'http_header_accept_encoding_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
http_header_accept_language = 'http_header_accept_language_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
device_id = 'device_id_example' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
geo_location = 'geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP.  (optional)

try:
    # Confirmation of the refund request by the PISP
    api_response = api_instance.refund_confirmation(x_request_id, message_create_date_time, refund_id, body=body, initiating_party_return_url=initiating_party_return_url, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundInitiationServiceV3ExtendedServicesApi->refund_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **refund_id** | **str**| The Id used by the Open Banking Service to refer to a refund.  | 
 **body** | [**ConfirmationRequest**](ConfirmationRequest.md)|  | [optional] 
 **initiating_party_return_url** | **str**| The callback URL for the redirection back to the Initiating Party after authorization.  | [optional] 
 **last_login** | **datetime**| PSU Session information.  The time when the PSU last logged in with the TPP.  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| PSU Session information.  The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **http_method** | **str**| PSU Session information.  HTTP method used at the PSU-TPP interface. Available values - GET, POST, PUT, DELETE.  | [optional] 
 **http_header_user_agent** | **str**| PSU Session information.  The forwarded Agent header field of the HTTP request between PSU and TPP.  | [optional] 
 **http_header_referer** | **str**| PSU Session information.  | [optional] 
 **http_header_accept** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **http_header_accept_charset** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **http_header_accept_encoding** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **http_header_accept_language** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **device_id** | **str**| UUID (Universally Unique Identifier) for a device, which is used by the PSU. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP.  | [optional] 

### Return type

[**RefundConfirmationResponse**](RefundConfirmationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_identification**
> RefundIdentificationResponse refund_identification(x_request_id, message_create_date_time, refund_id, body=body)

Refund identification request

Use this operation to identify a PSU in decoupled approach. The response of the post refunds API will provide a link to this api in the 'PostIdentificationForDecoupled' field if this step is required. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RefundInitiationServiceV3ExtendedServicesApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
refund_id = 'refund_id_example' # str | The Id used by the Open Banking Service to refer to a refund. 
body = swagger_client.PaymentIdentificationRequest() # PaymentIdentificationRequest |  (optional)

try:
    # Refund identification request
    api_response = api_instance.refund_identification(x_request_id, message_create_date_time, refund_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundInitiationServiceV3ExtendedServicesApi->refund_identification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **refund_id** | **str**| The Id used by the Open Banking Service to refer to a refund.  | 
 **body** | [**PaymentIdentificationRequest**](PaymentIdentificationRequest.md)|  | [optional] 

### Return type

[**RefundIdentificationResponse**](RefundIdentificationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_initiate**
> RefundInitiationResponse refund_initiate(x_request_id, message_create_date_time, body=body, initiating_party_return_url=initiating_party_return_url, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location, confirm=confirm)

Refund initiation request

Use this operation to initiate an order for refunds containing more than 1 refund instruction. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RefundInitiationServiceV3ExtendedServicesApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
body = swagger_client.RefundInitiationRequest() # RefundInitiationRequest |  (optional)
initiating_party_return_url = 'initiating_party_return_url_example' # str | The callback URL for the redirection back to the Initiating Party after authorization.  (optional)
use_authorisation_landing_pages = false # bool | If true, the Bank Selection Interface provided by Open Banking Service will be used to request required information from the PSU directly.  (optional) (default to false)
locale = 'locale_example' # str | 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  (optional)
last_login = '2013-10-20T19:20:30+01:00' # datetime | PSU Session information.  The time when the PSU last logged in with the TPP.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
psu_ip_port = 'psu_ip_port_example' # str | PSU Session information.  The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  (optional)
http_method = 'http_method_example' # str | PSU Session information.  HTTP method used at the PSU-TPP interface. Available values - GET, POST, PUT, DELETE.  (optional)
http_header_user_agent = 'http_header_user_agent_example' # str | PSU Session information.  The forwarded Agent header field of the HTTP request between PSU and TPP.  (optional)
http_header_referer = 'http_header_referer_example' # str | PSU Session information.  (optional)
http_header_accept = 'http_header_accept_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
http_header_accept_charset = 'http_header_accept_charset_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
http_header_accept_encoding = 'http_header_accept_encoding_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
http_header_accept_language = 'http_header_accept_language_example' # str | PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  (optional)
device_id = 'device_id_example' # str | UUID (Universally Unique Identifier) for a device, which is used by the PSU. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  (optional)
geo_location = 'geo_location_example' # str | The forwarded Geo Location of the corresponding http request between PSU and TPP.  (optional)
confirm = 'confirm_example' # str | If set to 'true' the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP. <br>**Note:** This field is only applicable when the notification service is used by the Initiating Party to receive the status of the payment. When the notification is not used this flag can be set in the GET status API.  (optional)

try:
    # Refund initiation request
    api_response = api_instance.refund_initiate(x_request_id, message_create_date_time, body=body, initiating_party_return_url=initiating_party_return_url, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location, confirm=confirm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundInitiationServiceV3ExtendedServicesApi->refund_initiate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **body** | [**RefundInitiationRequest**](RefundInitiationRequest.md)|  | [optional] 
 **initiating_party_return_url** | **str**| The callback URL for the redirection back to the Initiating Party after authorization.  | [optional] 
 **use_authorisation_landing_pages** | **bool**| If true, the Bank Selection Interface provided by Open Banking Service will be used to request required information from the PSU directly.  | [optional] [default to false]
 **locale** | **str**| 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  | [optional] 
 **last_login** | **datetime**| PSU Session information.  The time when the PSU last logged in with the TPP.  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **psu_ip_port** | **str**| PSU Session information.  The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **http_method** | **str**| PSU Session information.  HTTP method used at the PSU-TPP interface. Available values - GET, POST, PUT, DELETE.  | [optional] 
 **http_header_user_agent** | **str**| PSU Session information.  The forwarded Agent header field of the HTTP request between PSU and TPP.  | [optional] 
 **http_header_referer** | **str**| PSU Session information.  | [optional] 
 **http_header_accept** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **http_header_accept_charset** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **http_header_accept_encoding** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **http_header_accept_language** | **str**| PSU Session information.  The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP.  | [optional] 
 **device_id** | **str**| UUID (Universally Unique Identifier) for a device, which is used by the PSU. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID need to be unaltered until removal from device.  | [optional] 
 **geo_location** | **str**| The forwarded Geo Location of the corresponding http request between PSU and TPP.  | [optional] 
 **confirm** | **str**| If set to &#x27;true&#x27; the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP. &lt;br&gt;**Note:** This field is only applicable when the notification service is used by the Initiating Party to receive the status of the payment. When the notification is not used this flag can be set in the GET status API.  | [optional] 

### Return type

[**RefundInitiationResponse**](RefundInitiationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_status**
> RefundStatusResponse refund_status(refund_id, x_request_id, message_create_date_time, confirm=confirm, psu_ip_address=psu_ip_address)

Status of the refund

Use this operation to retrieve the status of a refund. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RefundInitiationServiceV3ExtendedServicesApi(swagger_client.ApiClient(configuration))
refund_id = 'refund_id_example' # str | The Id used by the Open Banking Service to refer to a refund. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
confirm = 'confirm_example' # str | If set to 'true' the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Status of the refund
    api_response = api_instance.refund_status(refund_id, x_request_id, message_create_date_time, confirm=confirm, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundInitiationServiceV3ExtendedServicesApi->refund_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The Id used by the Open Banking Service to refer to a refund.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **confirm** | **str**| If set to &#x27;true&#x27; the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP.  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**RefundStatusResponse**](RefundStatusResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


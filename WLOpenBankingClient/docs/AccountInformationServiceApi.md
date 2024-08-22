# swagger_client.AccountInformationServiceApi

All URIs are relative to *https://xs2a.awltest.de/xs2a/routingservice/services/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts**](AccountInformationServiceApi.md#accounts) | **GET** /ob/ais/v3/psus/{psuId}/aspsps/{aspspId}/accounts | Lists all accounts that are consented by the PSU for a specific ASPSP
[**authorisation**](AccountInformationServiceApi.md#authorisation) | **POST** /ob/ais/v3/psus/{psuId}/consents/{consentId}/authorisations | Start the authorisation process for a consent
[**authorisation_update**](AccountInformationServiceApi.md#authorisation_update) | **PUT** /ob/ais/v3/psus/{psuId}/consents/{consentId}/authorisations/{authorisationId} | Consent authorisation update
[**balances**](AccountInformationServiceApi.md#balances) | **GET** /ob/ais/v3/psus/{psuId}/aspsps/{aspspId}/accounts/{accountId}/balances | Get balances for a specific PSU&#x27;s account
[**consent_extended**](AccountInformationServiceApi.md#consent_extended) | **POST** /ob/ais/v3/psus/{psuId}/consents | Initiates the consent request, with additional options
[**identification**](AccountInformationServiceApi.md#identification) | **POST** /ob/ais/v3/psus/{psuId}/consents/{consentId}/identification | PSU identification request
[**revoke**](AccountInformationServiceApi.md#revoke) | **DELETE** /ob/ais/v3/psus/{psuId}/consents/{consentId} | Revoke the consent for a specific PSU
[**status**](AccountInformationServiceApi.md#status) | **GET** /ob/ais/v3/psus/{psuId}/consents/{consentId}/status | Get the status of a consent for a specific PSU
[**transactions**](AccountInformationServiceApi.md#transactions) | **GET** /ob/ais/v3/psus/{psuId}/aspsps/{aspspId}/accounts/{accountId}/transactions | Get the list of transactions for a specific PSU&#x27;s&#x27; account
[**transactionsdownload**](AccountInformationServiceApi.md#transactionsdownload) | **GET** /ob/ais/v3/download/psus/{psuId}/aspsps/{aspspId}/accounts/{accountId}/transactions | Get the list of transactions for a specific PSU&#x27;s&#x27; account as a download

# **accounts**
> GetAccountsResponse accounts(psu_id, aspsp_id, x_request_id, message_create_date_time, page=page, total_pages=total_pages, psu_ip_address=psu_ip_address)

Lists all accounts that are consented by the PSU for a specific ASPSP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
aspsp_id = 'aspsp_id_example' # str | ASPSP ID. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
page = 'page_example' # str | Used to retrieve a specific page in case the result is  paginated. The value can be first, last, prev, next or a  numerical value to request for a dedicated result page.  (optional)
total_pages = 56 # int | Used to limit the number of total pages retrieved by one request, if the result is paginated by the ASPSP. (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Lists all accounts that are consented by the PSU for a specific ASPSP
    api_response = api_instance.accounts(psu_id, aspsp_id, x_request_id, message_create_date_time, page=page, total_pages=total_pages, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **aspsp_id** | **str**| ASPSP ID.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **page** | **str**| Used to retrieve a specific page in case the result is  paginated. The value can be first, last, prev, next or a  numerical value to request for a dedicated result page.  | [optional] 
 **total_pages** | **int**| Used to limit the number of total pages retrieved by one request, if the result is paginated by the ASPSP. | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**GetAccountsResponse**](GetAccountsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorisation**
> ConsentAuthorisationResponse authorisation(x_request_id, message_create_date_time, psu_id, consent_id, body=body, psu_ip_address=psu_ip_address)

Start the authorisation process for a consent

Use this operation to authorize a PSU in multilevel authorization approach.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
consent_id = 'consent_id_example' # str | Id of the consent as received in the response to POST consents. 
body = swagger_client.ConsentAuthorisationRequest() # ConsentAuthorisationRequest |  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Start the authorisation process for a consent
    api_response = api_instance.authorisation(x_request_id, message_create_date_time, psu_id, consent_id, body=body, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **consent_id** | **str**| Id of the consent as received in the response to POST consents.  | 
 **body** | [**ConsentAuthorisationRequest**](ConsentAuthorisationRequest.md)|  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**ConsentAuthorisationResponse**](ConsentAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorisation_update**
> ConsentAuthorisationUpdateResponse authorisation_update(x_request_id, message_create_date_time, psu_id, consent_id, authorisation_id, body=body, psu_ip_address=psu_ip_address)

Consent authorisation update

Use this operation to update the authorization. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
consent_id = 'consent_id_example' # str | Id of the consent as received in the response to POST consents. 
authorisation_id = 'authorisation_id_example' # str | Id of the authorization as received in the response to the previous request in the corresponding Link. 
body = swagger_client.ConsentAuthorisationUpdateRequest() # ConsentAuthorisationUpdateRequest |  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Consent authorisation update
    api_response = api_instance.authorisation_update(x_request_id, message_create_date_time, psu_id, consent_id, authorisation_id, body=body, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->authorisation_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **consent_id** | **str**| Id of the consent as received in the response to POST consents.  | 
 **authorisation_id** | **str**| Id of the authorization as received in the response to the previous request in the corresponding Link.  | 
 **body** | [**ConsentAuthorisationUpdateRequest**](ConsentAuthorisationUpdateRequest.md)|  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**ConsentAuthorisationUpdateResponse**](ConsentAuthorisationUpdateResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balances**
> GetBalancesResponse balances(psu_id, aspsp_id, account_id, x_request_id, message_create_date_time, page=page, total_pages=total_pages, psu_ip_address=psu_ip_address)

Get balances for a specific PSU's account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
aspsp_id = 'aspsp_id_example' # str | ASPSP ID. 
account_id = 'account_id_example' # str | Id of the account of the PSU as retrieved form the GET accounts response. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
page = 'page_example' # str | Used to retrieve a specific page in case the result is  paginated. The value can be first, last, prev, next or a  numerical value to request for a dedicated result page.  (optional)
total_pages = 56 # int | Used to limit the number of total pages retrieved by one request, if the result is paginated by the ASPSP. (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Get balances for a specific PSU's account
    api_response = api_instance.balances(psu_id, aspsp_id, account_id, x_request_id, message_create_date_time, page=page, total_pages=total_pages, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **aspsp_id** | **str**| ASPSP ID.  | 
 **account_id** | **str**| Id of the account of the PSU as retrieved form the GET accounts response.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **page** | **str**| Used to retrieve a specific page in case the result is  paginated. The value can be first, last, prev, next or a  numerical value to request for a dedicated result page.  | [optional] 
 **total_pages** | **int**| Used to limit the number of total pages retrieved by one request, if the result is paginated by the ASPSP. | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**GetBalancesResponse**](GetBalancesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consent_extended**
> ConsentResponse consent_extended(x_request_id, message_create_date_time, psu_id, body=body, initiating_party_notification_url=initiating_party_notification_url, notification_version=notification_version, initiating_party_return_url=initiating_party_return_url, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, app_redirect_preferred=app_redirect_preferred, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location, use_implicit_pre_auth_combined=use_implicit_pre_auth_combined)

Initiates the consent request, with additional options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
body = swagger_client.ConsentRequest() # ConsentRequest |  (optional)
initiating_party_notification_url = 'initiating_party_notification_url_example' # str | The URL which will be used for notification service requests. The Open Banking Service supports two ways in which this field can be filled: * **Option A)** with an URL ending on /v2 or /v3, indicating the version of the Notification API implemented by the Initiating Party. In this case the URL called for notifications will be extended with /notification/status by the Open Banking Service. The 'NotificationVersion' field MUST NOT be filled. * **Option B)** with a full URL. The version information MUST BE provided in the 'NotificationVersion' field. In this case the provided URL will not be extended, and used as-is.  (optional)
notification_version = 'notification_version_example' # str | The version which shall be used for notification service requests. The version is either v2 or v3.  If the NotificationVersion is given: -  The URLs for notification endpoints must be provided as full URLs. -  No endpoint specific extension will be added when calling out for notifications.  See the description of InitiatingPartyNotificationUrl for more information.  (optional)
initiating_party_return_url = 'initiating_party_return_url_example' # str | The callback URL for the redirection back to the Initiating Party after authorization.  (optional)
use_authorisation_landing_pages = false # bool | If true, the Bank Selection Interface provided by Open Banking Service will be used to request required information from the PSU directly.  (optional) (default to false)
locale = 'locale_example' # str | 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  (optional)
app_redirect_preferred = false # bool | Indicates whether the user uses mobile device\\tablet or PC  (optional) (default to false)
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
use_implicit_pre_auth_combined = false # bool | To trigger such scope request towards the ASPSP  (optional) (default to false)

try:
    # Initiates the consent request, with additional options
    api_response = api_instance.consent_extended(x_request_id, message_create_date_time, psu_id, body=body, initiating_party_notification_url=initiating_party_notification_url, notification_version=notification_version, initiating_party_return_url=initiating_party_return_url, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, app_redirect_preferred=app_redirect_preferred, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location, use_implicit_pre_auth_combined=use_implicit_pre_auth_combined)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->consent_extended: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **body** | [**ConsentRequest**](ConsentRequest.md)|  | [optional] 
 **initiating_party_notification_url** | **str**| The URL which will be used for notification service requests. The Open Banking Service supports two ways in which this field can be filled: * **Option A)** with an URL ending on /v2 or /v3, indicating the version of the Notification API implemented by the Initiating Party. In this case the URL called for notifications will be extended with /notification/status by the Open Banking Service. The &#x27;NotificationVersion&#x27; field MUST NOT be filled. * **Option B)** with a full URL. The version information MUST BE provided in the &#x27;NotificationVersion&#x27; field. In this case the provided URL will not be extended, and used as-is.  | [optional] 
 **notification_version** | **str**| The version which shall be used for notification service requests. The version is either v2 or v3.  If the NotificationVersion is given: -  The URLs for notification endpoints must be provided as full URLs. -  No endpoint specific extension will be added when calling out for notifications.  See the description of InitiatingPartyNotificationUrl for more information.  | [optional] 
 **initiating_party_return_url** | **str**| The callback URL for the redirection back to the Initiating Party after authorization.  | [optional] 
 **use_authorisation_landing_pages** | **bool**| If true, the Bank Selection Interface provided by Open Banking Service will be used to request required information from the PSU directly.  | [optional] [default to false]
 **locale** | **str**| 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  | [optional] 
 **app_redirect_preferred** | **bool**| Indicates whether the user uses mobile device\\tablet or PC  | [optional] [default to false]
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
 **use_implicit_pre_auth_combined** | **bool**| To trigger such scope request towards the ASPSP  | [optional] [default to false]

### Return type

[**ConsentResponse**](ConsentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identification**
> ConsentIdentificationResponse identification(x_request_id, message_create_date_time, psu_id, consent_id, body=body, psu_ip_address=psu_ip_address)

PSU identification request

Use this operation to identify a PSU in a decoupled approach. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
consent_id = 'consent_id_example' # str | Id of the consent as received in the response to POST consents. 
body = swagger_client.ConsentIdentificationRequest() # ConsentIdentificationRequest |  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # PSU identification request
    api_response = api_instance.identification(x_request_id, message_create_date_time, psu_id, consent_id, body=body, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->identification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **consent_id** | **str**| Id of the consent as received in the response to POST consents.  | 
 **body** | [**ConsentIdentificationRequest**](ConsentIdentificationRequest.md)|  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**ConsentIdentificationResponse**](ConsentIdentificationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke**
> revoke(psu_id, consent_id, x_request_id, message_create_date_time, psu_ip_address=psu_ip_address)

Revoke the consent for a specific PSU

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
consent_id = 'consent_id_example' # str | Id of the consent as received in the response to POST consents. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Revoke the consent for a specific PSU
    api_instance.revoke(psu_id, consent_id, x_request_id, message_create_date_time, psu_ip_address=psu_ip_address)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **consent_id** | **str**| Id of the consent as received in the response to POST consents.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> ConsentDetailedInformation status(psu_id, consent_id, x_request_id, message_create_date_time, psu_ip_address=psu_ip_address)

Get the status of a consent for a specific PSU

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
consent_id = 'consent_id_example' # str | Id of the consent as received in the response to POST consents. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Get the status of a consent for a specific PSU
    api_response = api_instance.status(psu_id, consent_id, x_request_id, message_create_date_time, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **consent_id** | **str**| Id of the consent as received in the response to POST consents.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**ConsentDetailedInformation**](ConsentDetailedInformation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions**
> GetTransactionsResponse transactions(psu_id, aspsp_id, account_id, x_request_id, message_create_date_time, date_from=date_from, date_to=date_to, page=page, total_pages=total_pages, psu_ip_address=psu_ip_address)

Get the list of transactions for a specific PSU's' account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
aspsp_id = 'aspsp_id_example' # str | ASPSP ID. 
account_id = 'account_id_example' # str | Id of the account of the PSU as retrieved form the GET accounts response. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
date_from = 'date_from_example' # str | Date and time. All transactions on this date are included in the result. If no time is filled it will be set to 00:00. If the ASPSP doesn’t support time, the time part is omitted.  (optional)
date_to = 'date_to_example' # str | Date and time, transactions up to this date are included. So transaction on this date are not included in the result.  (optional)
page = 'page_example' # str | Used to retrieve a specific page in case the result is  paginated. The value can be first, last, prev, next or a  numerical value to request for a dedicated result page.  (optional)
total_pages = 56 # int | Used to limit the number of total pages retrieved by one request, if the result is paginated by the ASPSP. (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Get the list of transactions for a specific PSU's' account
    api_response = api_instance.transactions(psu_id, aspsp_id, account_id, x_request_id, message_create_date_time, date_from=date_from, date_to=date_to, page=page, total_pages=total_pages, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **aspsp_id** | **str**| ASPSP ID.  | 
 **account_id** | **str**| Id of the account of the PSU as retrieved form the GET accounts response.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **date_from** | **str**| Date and time. All transactions on this date are included in the result. If no time is filled it will be set to 00:00. If the ASPSP doesn’t support time, the time part is omitted.  | [optional] 
 **date_to** | **str**| Date and time, transactions up to this date are included. So transaction on this date are not included in the result.  | [optional] 
 **page** | **str**| Used to retrieve a specific page in case the result is  paginated. The value can be first, last, prev, next or a  numerical value to request for a dedicated result page.  | [optional] 
 **total_pages** | **int**| Used to limit the number of total pages retrieved by one request, if the result is paginated by the ASPSP. | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**GetTransactionsResponse**](GetTransactionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactionsdownload**
> GetTransactionsResponse transactionsdownload(psu_id, aspsp_id, account_id, dl, x_request_id, psu_ip_address=psu_ip_address)

Get the list of transactions for a specific PSU's' account as a download

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountInformationServiceApi(swagger_client.ApiClient(configuration))
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
aspsp_id = 'aspsp_id_example' # str | ASPSP ID. 
account_id = 'account_id_example' # str | Id of the account of the PSU as retrieved form the GET accounts response. 
dl = 'dl_example' # str | Download ID as given in the download link of GET transactions.
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Get the list of transactions for a specific PSU's' account as a download
    api_response = api_instance.transactionsdownload(psu_id, aspsp_id, account_id, dl, x_request_id, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceApi->transactionsdownload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **aspsp_id** | **str**| ASPSP ID.  | 
 **account_id** | **str**| Id of the account of the PSU as retrieved form the GET accounts response.  | 
 **dl** | **str**| Download ID as given in the download link of GET transactions. | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**GetTransactionsResponse**](GetTransactionsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


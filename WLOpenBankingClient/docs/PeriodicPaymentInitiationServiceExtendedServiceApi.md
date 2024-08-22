# swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi

All URIs are relative to *https://xs2a.awltest.de/xs2a/routingservice/services/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**periodic_payment_authorisation**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_authorisation) | **POST** /ob/pis/v3/periodic-payments/{paymentId}/authorisations | Payment authorisation request
[**periodic_payment_authorisation_update**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_authorisation_update) | **PUT** /ob/pis/v3/periodic-payments/{paymentId}/authorisations/{authorisationId} | Payment authorisation request
[**periodic_payment_cancellation**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_cancellation) | **DELETE** /ob/pis/v3/periodic-payments/{paymentId} | Payment cancellation request
[**periodic_payment_cancellation_authorisation**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_cancellation_authorisation) | **POST** /ob/pis/v3/periodic-payments/{paymentId}/cancellation-authorisations | Payment cancellation authorisation request
[**periodic_payment_cancellation_authorisation_update**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_cancellation_authorisation_update) | **PUT** /ob/pis/v3/periodic-payments/{paymentId}/cancellation-authorisations/{authorisationId} | Payment cancellation authorisation request update
[**periodic_payment_cancellation_identification**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_cancellation_identification) | **POST** /ob/pis/v3/periodic-payments/{paymentId}/cancellation-identification | Payment cancellation identification request
[**periodic_payment_confirmation**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_confirmation) | **POST** /ob/pis/v3/periodic-payments/{paymentId}/confirmation | Confirmation of the payment request by the PISP
[**periodic_payment_identification**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_identification) | **POST** /ob/pis/v3/periodic-payments/{paymentId}/identification | Payment identification request
[**periodic_payment_initiate**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_initiate) | **POST** /ob/pis/v3/periodic-payments | Payment initiation request
[**periodic_payment_status**](PeriodicPaymentInitiationServiceExtendedServiceApi.md#periodic_payment_status) | **GET** /ob/pis/v3/periodic-payments/{paymentId}/status | Status of the payment request

# **periodic_payment_authorisation**
> PaymentAuthorisationResponse periodic_payment_authorisation(x_request_id, message_create_date_time, payment_id, body=body)

Payment authorisation request

Use this operation to authorise a PSU explicitly. This has to be used if multiple PSU's have to authorise the payment. Background information: If only one PSU has to authorise, this step is started implicitly by the post payments api. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
body = swagger_client.PaymentAuthorisationRequest() # PaymentAuthorisationRequest |  (optional)

try:
    # Payment authorisation request
    api_response = api_instance.periodic_payment_authorisation(x_request_id, message_create_date_time, payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **body** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)|  | [optional] 

### Return type

[**PaymentAuthorisationResponse**](PaymentAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_authorisation_update**
> PaymentAuthorisationResponse periodic_payment_authorisation_update(x_request_id, message_create_date_time, payment_id, authorisation_id, body=body)

Payment authorisation request

Use this operation to change the authorisation resource. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
authorisation_id = 'authorisation_id_example' # str | The Id used by the Open Banking Service to refer to an authorisation resource. 
body = swagger_client.PaymentAuthorisationUpdateRequest() # PaymentAuthorisationUpdateRequest |  (optional)

try:
    # Payment authorisation request
    api_response = api_instance.periodic_payment_authorisation_update(x_request_id, message_create_date_time, payment_id, authorisation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_authorisation_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **authorisation_id** | **str**| The Id used by the Open Banking Service to refer to an authorisation resource.  | 
 **body** | [**PaymentAuthorisationUpdateRequest**](PaymentAuthorisationUpdateRequest.md)|  | [optional] 

### Return type

[**PaymentAuthorisationResponse**](PaymentAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_cancellation**
> PaymentCancellationResponse periodic_payment_cancellation(payment_id, x_request_id, message_create_date_time, initiating_party_return_url=initiating_party_return_url, aspsp_psu_id=aspsp_psu_id, aspsp_psu_id_type=aspsp_psu_id_type, aspsp_psu_corporate_id=aspsp_psu_corporate_id, aspsp_psu_corporate_id_type=aspsp_psu_corporate_id_type, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, psu_ip_address=psu_ip_address)

Payment cancellation request

Use this operation to cancel a payment on behalf of the Payment Service User. Strong Customer Authentication might be required by the ASPSP, the response will indicate which step is required to complete the cancellation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
initiating_party_return_url = 'initiating_party_return_url_example' # str | The callback URL for the redirection back to the Initiating Party after authorization.  (optional)
aspsp_psu_id = 'aspsp_psu_id_example' # str | PSU’s Id at ASPSP. Allows the unique identification of the PSU at the ASPSP.  (optional)
aspsp_psu_id_type = 'aspsp_psu_id_type_example' # str | Type of the Aspsp PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  (optional)
aspsp_psu_corporate_id = 'aspsp_psu_corporate_id_example' # str | Identification of a Corporate in the Online Channels.  (optional)
aspsp_psu_corporate_id_type = 'aspsp_psu_corporate_id_type_example' # str | This is describing the type of the identification needed by the ASPSP to identify the PSUCorporate-ID type.  (optional)
use_authorisation_landing_pages = false # bool | If true, the Bank Selection Interface provided by Open Banking Service will be used to request required information from the PSU directly.  (optional) (default to false)
locale = 'locale_example' # str | 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)

try:
    # Payment cancellation request
    api_response = api_instance.periodic_payment_cancellation(payment_id, x_request_id, message_create_date_time, initiating_party_return_url=initiating_party_return_url, aspsp_psu_id=aspsp_psu_id, aspsp_psu_id_type=aspsp_psu_id_type, aspsp_psu_corporate_id=aspsp_psu_corporate_id, aspsp_psu_corporate_id_type=aspsp_psu_corporate_id_type, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, psu_ip_address=psu_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **initiating_party_return_url** | **str**| The callback URL for the redirection back to the Initiating Party after authorization.  | [optional] 
 **aspsp_psu_id** | **str**| PSU’s Id at ASPSP. Allows the unique identification of the PSU at the ASPSP.  | [optional] 
 **aspsp_psu_id_type** | **str**| Type of the Aspsp PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  | [optional] 
 **aspsp_psu_corporate_id** | **str**| Identification of a Corporate in the Online Channels.  | [optional] 
 **aspsp_psu_corporate_id_type** | **str**| This is describing the type of the identification needed by the ASPSP to identify the PSUCorporate-ID type.  | [optional] 
 **use_authorisation_landing_pages** | **bool**| If true, the Bank Selection Interface provided by Open Banking Service will be used to request required information from the PSU directly.  | [optional] [default to false]
 **locale** | **str**| 2-digit ISO-639 code for the language in which the Bank Selection Interface is displayed.  For special languages can be used 5-digit code like nl-BE, where first is ISO-639 langauge code and the second is ISO-3166 country code.  If not set, the language of the Bank Selection Interface is taken over from the end user’s browser configuration or the system configuration of the Bank Selection Interface server.  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 

### Return type

[**PaymentCancellationResponse**](PaymentCancellationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_cancellation_authorisation**
> PaymentAuthorisationResponse periodic_payment_cancellation_authorisation(x_request_id, message_create_date_time, payment_id, body=body)

Payment cancellation authorisation request

Use this operation to authorise a PSU explicitly. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
body = swagger_client.PaymentAuthorisationRequest() # PaymentAuthorisationRequest |  (optional)

try:
    # Payment cancellation authorisation request
    api_response = api_instance.periodic_payment_cancellation_authorisation(x_request_id, message_create_date_time, payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_cancellation_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **body** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)|  | [optional] 

### Return type

[**PaymentAuthorisationResponse**](PaymentAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_cancellation_authorisation_update**
> PaymentAuthorisationResponse periodic_payment_cancellation_authorisation_update(x_request_id, message_create_date_time, payment_id, authorisation_id, body=body)

Payment cancellation authorisation request update

Use this operation to update the authorisation resource. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
authorisation_id = 'authorisation_id_example' # str | The Id used by the Open Banking Service to refer to an authorisation resource. 
body = swagger_client.PaymentAuthorisationUpdateRequest() # PaymentAuthorisationUpdateRequest |  (optional)

try:
    # Payment cancellation authorisation request update
    api_response = api_instance.periodic_payment_cancellation_authorisation_update(x_request_id, message_create_date_time, payment_id, authorisation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_cancellation_authorisation_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **authorisation_id** | **str**| The Id used by the Open Banking Service to refer to an authorisation resource.  | 
 **body** | [**PaymentAuthorisationUpdateRequest**](PaymentAuthorisationUpdateRequest.md)|  | [optional] 

### Return type

[**PaymentAuthorisationResponse**](PaymentAuthorisationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_cancellation_identification**
> PaymentIdentificationResponse periodic_payment_cancellation_identification(x_request_id, message_create_date_time, payment_id, body=body)

Payment cancellation identification request

Use this operation to identify a PSU in decoupled approach. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
body = swagger_client.PaymentIdentificationRequest() # PaymentIdentificationRequest |  (optional)

try:
    # Payment cancellation identification request
    api_response = api_instance.periodic_payment_cancellation_identification(x_request_id, message_create_date_time, payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_cancellation_identification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **body** | [**PaymentIdentificationRequest**](PaymentIdentificationRequest.md)|  | [optional] 

### Return type

[**PaymentIdentificationResponse**](PaymentIdentificationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_confirmation**
> PaymentConfirmationResponse periodic_payment_confirmation(x_request_id, message_create_date_time, payment_id, body=body)

Confirmation of the payment request by the PISP

This Api is used to confirm a payment. Confirmation is required when the link 'ConfirmationRequired' is returned. Confirmation of a payment can be required in two cases 1) When its required by the ASPSP standard 2) when a payment fee is involved. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
body = swagger_client.ConfirmationRequest() # ConfirmationRequest |  (optional)

try:
    # Confirmation of the payment request by the PISP
    api_response = api_instance.periodic_payment_confirmation(x_request_id, message_create_date_time, payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **body** | [**ConfirmationRequest**](ConfirmationRequest.md)|  | [optional] 

### Return type

[**PaymentConfirmationResponse**](PaymentConfirmationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_identification**
> PaymentIdentificationResponse periodic_payment_identification(x_request_id, message_create_date_time, payment_id, body=body)

Payment identification request

Use this operation to identify a PSU in decoupled approach. The response of the post payments api will provide a link to this api in the 'PostIdentificationForDecoupled' field if this step is required. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
body = swagger_client.PaymentIdentificationRequest() # PaymentIdentificationRequest |  (optional)

try:
    # Payment identification request
    api_response = api_instance.periodic_payment_identification(x_request_id, message_create_date_time, payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_identification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **body** | [**PaymentIdentificationRequest**](PaymentIdentificationRequest.md)|  | [optional] 

### Return type

[**PaymentIdentificationResponse**](PaymentIdentificationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_initiate**
> PaymentInitiationResponse periodic_payment_initiate(x_request_id, message_create_date_time, psu_id, body=body, initiating_party_return_url=initiating_party_return_url, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, app_redirect_preferred=app_redirect_preferred, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location, signature=signature, digest=digest, confirm=confirm)

Payment initiation request

Use this operation to initiate a payment on behalf of the Payment Service User. Strong customer authentication might be required by the ASPSP, the response will indicate which step is required to complete the payment. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
psu_id = 'psu_id_example' # str | This field can be filled with an ID from the Initiating Party which refers to the PSU. 
body = swagger_client.PeriodicPaymentInitiationRequest() # PeriodicPaymentInitiationRequest |  (optional)
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
signature = 'signature_example' # str | Conditionally required for iDEAL payments. The signature in the request should include a keyId with the value of fingerprint of the certificate  (optional)
digest = 'digest_example' # str | Is contained if and only if the `Signature` element is contained in the header of the request. (optional)
confirm = 'confirm_example' # str | If set to 'true' the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP. <br>**Note:** This field is only applicable when the notification service is used by the Initiating Party to receive the status of the payment. When the notification is not used this flag can be set in the GET status API.  (optional)

try:
    # Payment initiation request
    api_response = api_instance.periodic_payment_initiate(x_request_id, message_create_date_time, psu_id, body=body, initiating_party_return_url=initiating_party_return_url, use_authorisation_landing_pages=use_authorisation_landing_pages, locale=locale, app_redirect_preferred=app_redirect_preferred, last_login=last_login, psu_ip_address=psu_ip_address, psu_ip_port=psu_ip_port, http_method=http_method, http_header_user_agent=http_header_user_agent, http_header_referer=http_header_referer, http_header_accept=http_header_accept, http_header_accept_charset=http_header_accept_charset, http_header_accept_encoding=http_header_accept_encoding, http_header_accept_language=http_header_accept_language, device_id=device_id, geo_location=geo_location, signature=signature, digest=digest, confirm=confirm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_initiate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **psu_id** | **str**| This field can be filled with an ID from the Initiating Party which refers to the PSU.  | 
 **body** | [**PeriodicPaymentInitiationRequest**](PeriodicPaymentInitiationRequest.md)|  | [optional] 
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
 **signature** | **str**| Conditionally required for iDEAL payments. The signature in the request should include a keyId with the value of fingerprint of the certificate  | [optional] 
 **digest** | **str**| Is contained if and only if the &#x60;Signature&#x60; element is contained in the header of the request. | [optional] 
 **confirm** | **str**| If set to &#x27;true&#x27; the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP. &lt;br&gt;**Note:** This field is only applicable when the notification service is used by the Initiating Party to receive the status of the payment. When the notification is not used this flag can be set in the GET status API.  | [optional] 

### Return type

[**PaymentInitiationResponse**](PaymentInitiationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **periodic_payment_status**
> PaymentDetailedInformation periodic_payment_status(payment_id, x_request_id, message_create_date_time, confirm=confirm, psu_ip_address=psu_ip_address, signature=signature, digest=digest)

Status of the payment request

Use this operation to retrieve the status of a payment. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PeriodicPaymentInitiationServiceExtendedServiceApi(swagger_client.ApiClient(configuration))
payment_id = 'payment_id_example' # str | The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier. 
x_request_id = 'x_request_id_example' # str | UUID for unique request identification. 
message_create_date_time = '2013-10-20T19:20:30+01:00' # datetime | The message create date time.  ISO 8601 DateTime. 
confirm = 'confirm_example' # str | If set to 'true' the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP.  (optional)
psu_ip_address = 'psu_ip_address_example' # str | PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  (optional)
signature = 'signature_example' # str | Conditionally required for iDEAL payments. The signature in the request should include a keyId with the value of fingerprint of the certificate  (optional)
digest = 'digest_example' # str | Is contained if and only if the `Signature` element is contained in the header of the request. (optional)

try:
    # Status of the payment request
    api_response = api_instance.periodic_payment_status(payment_id, x_request_id, message_create_date_time, confirm=confirm, psu_ip_address=psu_ip_address, signature=signature, digest=digest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodicPaymentInitiationServiceExtendedServiceApi->periodic_payment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The Id used by the Open Banking Service to refer to a payment.  Optionally the payment can also be refered by the **InitiatingPartyReferenceId** or the **EndToEndId**, to do so start with **ref** or **e2e** prefixes followed by the respective identifier.  | 
 **x_request_id** | **str**| UUID for unique request identification.  | 
 **message_create_date_time** | **datetime**| The message create date time.  ISO 8601 DateTime.  | 
 **confirm** | **str**| If set to &#x27;true&#x27; the transaction will be immediately confirmed by the Open Banking Service if confirmation of the payment by the Initiating Party is required by the ASPSP.  | [optional] 
 **psu_ip_address** | **str**| PSU Session information.  The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP . It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
 **signature** | **str**| Conditionally required for iDEAL payments. The signature in the request should include a keyId with the value of fingerprint of the certificate  | [optional] 
 **digest** | **str**| Is contained if and only if the &#x60;Signature&#x60; element is contained in the header of the request. | [optional] 

### Return type

[**PaymentDetailedInformation**](PaymentDetailedInformation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


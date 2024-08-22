# ScaMethods

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** | Type of the SCA authentication method. The following methods are commonly seen coming from the ASPSP: -  SMS_OTP: The PSU will receive a One Time Password via SMS -  CHIP_OTP: The PSU will be presented with a picture or text to create a One Time Password using their bank card -  PHOTO_OTP: The PSU will be presented with a picture to create a One Time Password -  PUSH_OTP: The PSU will receive a One Time Password via push notification on their mobile device -  SMTP_OTP: The PSU will receive a One Time Password via email  | 
**authentication_method_id** | **str** | An identification provided by the ASPSP for the later identification of the authentication method selection.  | 
**version** | **str** | Depending on the AuthenticationType. This version can be used by differentiating authentication tools used within performing OTP generation in the same authentication type. This version can be referred to in the ASPSP&#x27;s documentation.  | [optional] 
**name** | **str** | This is the name of the authentication method defined by the PSU in the Online Banking frontend of the ASPSP. Alternatively this could be a description provided by the ASPSP like \&quot;SMS OTP on phone +49160 xxxxx 28\&quot;. This name shall be used by the TPP when presenting a list of authentication methods to the PSU, if available.  | [optional] 
**explanation** | **str** | Detailed information about the SCA method, meant for the PSU.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


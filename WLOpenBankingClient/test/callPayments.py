import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import datetime
from pprint import pprint
import uuid

import swagger_client
from swagger_client.models.permission_enum import PermissionEnum
from swagger_client.rest import ApiException

# Configure API key authorization: sso_auth
configuration = swagger_client.Configuration()
configuration.debug = True

api_client = swagger_client.ApiClient(configuration)
api_client.set_default_header(
    "Authorization", "Bearer 97fb13a74c712d8c7a50476e71769eaf"
)

api_instance = swagger_client.PaymentInitiationServiceApi(api_client)
# .AccountInformationServiceApi(api_client)
psuid = "123456"
aspspid = "20116"

amount = swagger_client.models.Amount(amount="100")
commonData = swagger_client.PaymentInitiationRequestBasic(amount=amount)
body = swagger_client.PaymentInitiationRequest(common_payment_data=commonData)
# body.psu_data.aspsp_id = aspspid
pprint(body)

try:
    # Requests by user id
    xreqid = str(uuid.uuid4())
    api_response = api_instance.payment_initiate(
        xreqid, datetime.datetime.now(), psuid, body=body
    )

    print("## answer ##")
    pprint(api_response)
    print("## end of answer ##")

    # print(api_response.links.redirect_url.href)
    # print(api_response.consent_id)
except ApiException as e:
    print(
        "Exception when calling PaymentInitiationServiceApi.payment_initiate: %s\n" % e
    )

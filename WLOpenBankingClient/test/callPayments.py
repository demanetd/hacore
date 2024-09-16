import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import datetime
from pprint import pprint
import uuid

import pis_client
from pis_client.rest import ApiException

# Configure API key authorization: sso_auth
configuration = pis_client.Configuration()
configuration.debug = True

api_client = pis_client.ApiClient(configuration)
api_client.set_default_header(
    "Authorization", "Bearer 97fb13a74c712d8c7a50476e71769eaf"
)

api_instance = pis_client.PaymentInitiationServiceApi(api_client)
psuid = "123456"
aspspid = "20116"

amount = pis_client.models.Amount(amount="100.0")
commonData = pis_client.PaymentInitiationRequestBasic(amount=amount)
body = pis_client.PaymentInitiationRequest(common_payment_data=commonData)
pprint(body)

try:
    # Requests by user id
    xreqid = str(uuid.uuid4())
    api_response = api_instance.payment_initiate(
        xreqid, datetime.datetime.now(), body=body
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

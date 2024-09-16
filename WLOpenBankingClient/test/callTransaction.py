import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import datetime
from pprint import pprint
import uuid

import ais_client
from ais_client.rest import ApiException

# Configure API key authorization: sso_auth
configuration = ais_client.Configuration()
configuration.debug = True

api_client = ais_client.ApiClient(configuration)
api_client.set_default_header("Authorization", "Bearer d5bd895a4080dbbb469a207460b6fca")

api_instance = ais_client.AccountInformationServiceApi(api_client)

try:
    # Requests by user id
    xreqid = str(uuid.uuid4())
    psuid = "123456"
    aspspid = "20101"
    accountid = "182760"
    api_response = api_instance.transactions(
        psuid, aspspid, accountid, xreqid, datetime.datetime.now()
    )

    print("## answer ##")
    pprint(api_response)
    print("## end of answer ##")

    # print(api_response.consent_status)
except ApiException as e:
    print(
        "Exception when calling AccountInformationServiceApi.consent_extended: %s\n" % e
    )

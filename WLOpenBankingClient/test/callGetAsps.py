import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, "/workspaces/hacore/WLOpenBankingClient")

import datetime
from pprint import pprint
import uuid

import reach_client
from reach_client.rest import ApiException

# Configure API key authorization: sso_auth
configuration = reach_client.Configuration()
# configuration.api_key['Authorization'] = '97fb13a74c712d8c7a50476e71769eaf'
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration.debug = True

api_client = reach_client.ApiClient(configuration)
api_client.set_default_header(
    "Authorization", "Bearer 97fb13a74c712d8c7a50476e71769eaf"
)

api_instance = reach_client.ReachDirectoryApi(api_client)

try:
    # Requests by user id
    xreqid = str(uuid.uuid4())
    api_response = api_instance.reach(
        xreqid,
        datetime.datetime.now(),
        "PIS",
        all_aspsp_specific_fields=True,
        all_details=True,
    )

    print("## answer ##")
    pprint(api_response)
    print("## end of answer ##")

    print(api_response.aspsp[1].aspsp_id)
except ApiException as e:
    print("Exception when calling ReachDirectoryApi->reach: %s\n" % e)

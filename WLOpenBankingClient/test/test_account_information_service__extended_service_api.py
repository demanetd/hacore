
"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import unittest

from swagger_client.api.account_information_service__extended_service_api import (
    AccountInformationServiceExtendedServiceApi,  # noqa: E501
)


class TestAccountInformationServiceExtendedServiceApi(unittest.TestCase):
    """AccountInformationServiceExtendedServiceApi unit test stubs"""

    def setUp(self):
        self.api = AccountInformationServiceExtendedServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_registration(self):
        """Test case for delete_registration

        Delete an existing registration  # noqa: E501
        """

    def test_get_registration_status(self):
        """Test case for get_registration_status

        Get an existing registration status  # noqa: E501
        """

    def test_post_consent_authorisation(self):
        """Test case for post_consent_authorisation

        Get the link to the IS for the consent authorisation  # noqa: E501
        """

    def test_put_registration(self):
        """Test case for put_registration

        Update an existing registration for the PSU  # noqa: E501
        """

    def test_registration(self):
        """Test case for registration

        POST a new registration resource for a specific product.  # noqa: E501
        """


if __name__ == '__main__':
    unittest.main()


"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ConsentIdentificationResponse:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'consent_id': 'str',
        'consent_status': 'ConsentStatusEnum',
        'auth_status': 'AuthStatusEnum',
        'links': 'Links',
        'psu_message': 'str'
    }

    attribute_map = {
        'consent_id': 'ConsentId',
        'consent_status': 'ConsentStatus',
        'auth_status': 'AuthStatus',
        'links': 'Links',
        'psu_message': 'PsuMessage'
    }

    def __init__(self, consent_id=None, consent_status=None, auth_status=None, links=None, psu_message=None):  # noqa: E501
        """ConsentIdentificationResponse - a model defined in Swagger"""  # noqa: E501
        self._consent_id = None
        self._consent_status = None
        self._auth_status = None
        self._links = None
        self._psu_message = None
        self.discriminator = None
        self.consent_id = consent_id
        self.consent_status = consent_status
        if auth_status is not None:
            self.auth_status = auth_status
        if links is not None:
            self.links = links
        if psu_message is not None:
            self.psu_message = psu_message

    @property
    def consent_id(self):
        """Gets the consent_id of this ConsentIdentificationResponse.  # noqa: E501

        Id generated by the Open Banking Service. This should be used to refer to this consent.   # noqa: E501

        :return: The consent_id of this ConsentIdentificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ConsentIdentificationResponse.

        Id generated by the Open Banking Service. This should be used to refer to this consent.   # noqa: E501

        :param consent_id: The consent_id of this ConsentIdentificationResponse.  # noqa: E501
        :type: str
        """
        if consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def consent_status(self):
        """Gets the consent_status of this ConsentIdentificationResponse.  # noqa: E501

        :return: The consent_status of this ConsentIdentificationResponse.  # noqa: E501
        :rtype: ConsentStatusEnum
        """
        return self._consent_status

    @consent_status.setter
    def consent_status(self, consent_status):
        """Sets the consent_status of this ConsentIdentificationResponse.

        :param consent_status: The consent_status of this ConsentIdentificationResponse.  # noqa: E501
        :type: ConsentStatusEnum
        """
        if consent_status is None:
            raise ValueError("Invalid value for `consent_status`, must not be `None`")  # noqa: E501

        self._consent_status = consent_status

    @property
    def auth_status(self):
        """Gets the auth_status of this ConsentIdentificationResponse.  # noqa: E501

        :return: The auth_status of this ConsentIdentificationResponse.  # noqa: E501
        :rtype: AuthStatusEnum
        """
        return self._auth_status

    @auth_status.setter
    def auth_status(self, auth_status):
        """Sets the auth_status of this ConsentIdentificationResponse.

        :param auth_status: The auth_status of this ConsentIdentificationResponse.  # noqa: E501
        :type: AuthStatusEnum
        """

        self._auth_status = auth_status

    @property
    def links(self):
        """Gets the links of this ConsentIdentificationResponse.  # noqa: E501

        :return: The links of this ConsentIdentificationResponse.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConsentIdentificationResponse.

        :param links: The links of this ConsentIdentificationResponse.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def psu_message(self):
        """Gets the psu_message of this ConsentIdentificationResponse.  # noqa: E501

        Text to be displayed to the PSU.   # noqa: E501

        :return: The psu_message of this ConsentIdentificationResponse.  # noqa: E501
        :rtype: str
        """
        return self._psu_message

    @psu_message.setter
    def psu_message(self, psu_message):
        """Sets the psu_message of this ConsentIdentificationResponse.

        Text to be displayed to the PSU.   # noqa: E501

        :param psu_message: The psu_message of this ConsentIdentificationResponse.  # noqa: E501
        :type: str
        """

        self._psu_message = psu_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConsentIdentificationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConsentIdentificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

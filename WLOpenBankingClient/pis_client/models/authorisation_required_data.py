# coding: utf-8

"""
    Open Banking Payment Initiation Service

    ### Introduction There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported.  #### PSD2 Sandbox Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

    OpenAPI spec version: 3.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AuthorisationRequiredData(object):
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
        'psu_credentials': 'list[PsuCredentials]',
        'sca_methods': 'list[ScaMethods]',
        'chosen_sca_method': 'ScaMethods',
        'challenge_data': 'ScaChallengeData'
    }

    attribute_map = {
        'psu_credentials': 'PsuCredentials',
        'sca_methods': 'ScaMethods',
        'chosen_sca_method': 'ChosenScaMethod',
        'challenge_data': 'ChallengeData'
    }

    def __init__(self, psu_credentials=None, sca_methods=None, chosen_sca_method=None, challenge_data=None):  # noqa: E501
        """AuthorisationRequiredData - a model defined in Swagger"""  # noqa: E501
        self._psu_credentials = None
        self._sca_methods = None
        self._chosen_sca_method = None
        self._challenge_data = None
        self.discriminator = None
        if psu_credentials is not None:
            self.psu_credentials = psu_credentials
        if sca_methods is not None:
            self.sca_methods = sca_methods
        if chosen_sca_method is not None:
            self.chosen_sca_method = chosen_sca_method
        if challenge_data is not None:
            self.challenge_data = challenge_data

    @property
    def psu_credentials(self):
        """Gets the psu_credentials of this AuthorisationRequiredData.  # noqa: E501

        List of credentials the PSU has on the ASPSP's system. The PSU has to provide the CredentialValue for each of these (Username & Password).   # noqa: E501

        :return: The psu_credentials of this AuthorisationRequiredData.  # noqa: E501
        :rtype: list[PsuCredentials]
        """
        return self._psu_credentials

    @psu_credentials.setter
    def psu_credentials(self, psu_credentials):
        """Sets the psu_credentials of this AuthorisationRequiredData.

        List of credentials the PSU has on the ASPSP's system. The PSU has to provide the CredentialValue for each of these (Username & Password).   # noqa: E501

        :param psu_credentials: The psu_credentials of this AuthorisationRequiredData.  # noqa: E501
        :type: list[PsuCredentials]
        """

        self._psu_credentials = psu_credentials

    @property
    def sca_methods(self):
        """Gets the sca_methods of this AuthorisationRequiredData.  # noqa: E501

        Array of available ScaMethods.   # noqa: E501

        :return: The sca_methods of this AuthorisationRequiredData.  # noqa: E501
        :rtype: list[ScaMethods]
        """
        return self._sca_methods

    @sca_methods.setter
    def sca_methods(self, sca_methods):
        """Sets the sca_methods of this AuthorisationRequiredData.

        Array of available ScaMethods.   # noqa: E501

        :param sca_methods: The sca_methods of this AuthorisationRequiredData.  # noqa: E501
        :type: list[ScaMethods]
        """

        self._sca_methods = sca_methods

    @property
    def chosen_sca_method(self):
        """Gets the chosen_sca_method of this AuthorisationRequiredData.  # noqa: E501


        :return: The chosen_sca_method of this AuthorisationRequiredData.  # noqa: E501
        :rtype: ScaMethods
        """
        return self._chosen_sca_method

    @chosen_sca_method.setter
    def chosen_sca_method(self, chosen_sca_method):
        """Sets the chosen_sca_method of this AuthorisationRequiredData.


        :param chosen_sca_method: The chosen_sca_method of this AuthorisationRequiredData.  # noqa: E501
        :type: ScaMethods
        """

        self._chosen_sca_method = chosen_sca_method

    @property
    def challenge_data(self):
        """Gets the challenge_data of this AuthorisationRequiredData.  # noqa: E501


        :return: The challenge_data of this AuthorisationRequiredData.  # noqa: E501
        :rtype: ScaChallengeData
        """
        return self._challenge_data

    @challenge_data.setter
    def challenge_data(self, challenge_data):
        """Sets the challenge_data of this AuthorisationRequiredData.


        :param challenge_data: The challenge_data of this AuthorisationRequiredData.  # noqa: E501
        :type: ScaChallengeData
        """

        self._challenge_data = challenge_data

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
        if issubclass(AuthorisationRequiredData, dict):
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
        if not isinstance(other, AuthorisationRequiredData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RelatedParties:
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
        'creditor_id': 'str',
        'ultimate_creditor': 'str',
        'ultimate_debtor': 'str'
    }

    attribute_map = {
        'creditor_id': 'CreditorId',
        'ultimate_creditor': 'UltimateCreditor',
        'ultimate_debtor': 'UltimateDebtor'
    }

    def __init__(self, creditor_id=None, ultimate_creditor=None, ultimate_debtor=None):  # noqa: E501
        """RelatedParties - a model defined in Swagger"""  # noqa: E501
        self._creditor_id = None
        self._ultimate_creditor = None
        self._ultimate_debtor = None
        self.discriminator = None
        if creditor_id is not None:
            self.creditor_id = creditor_id
        if ultimate_creditor is not None:
            self.ultimate_creditor = ultimate_creditor
        if ultimate_debtor is not None:
            self.ultimate_debtor = ultimate_debtor

    @property
    def creditor_id(self):
        """Gets the creditor_id of this RelatedParties.  # noqa: E501

        Identification of Creditors, e.g. a SEPA Creditor ID.   # noqa: E501

        :return: The creditor_id of this RelatedParties.  # noqa: E501
        :rtype: str
        """
        return self._creditor_id

    @creditor_id.setter
    def creditor_id(self, creditor_id):
        """Sets the creditor_id of this RelatedParties.

        Identification of Creditors, e.g. a SEPA Creditor ID.   # noqa: E501

        :param creditor_id: The creditor_id of this RelatedParties.  # noqa: E501
        :type: str
        """

        self._creditor_id = creditor_id

    @property
    def ultimate_creditor(self):
        """Gets the ultimate_creditor of this RelatedParties.  # noqa: E501

        Ultimate party to which an amount of money is due.   # noqa: E501

        :return: The ultimate_creditor of this RelatedParties.  # noqa: E501
        :rtype: str
        """
        return self._ultimate_creditor

    @ultimate_creditor.setter
    def ultimate_creditor(self, ultimate_creditor):
        """Sets the ultimate_creditor of this RelatedParties.

        Ultimate party to which an amount of money is due.   # noqa: E501

        :param ultimate_creditor: The ultimate_creditor of this RelatedParties.  # noqa: E501
        :type: str
        """

        self._ultimate_creditor = ultimate_creditor

    @property
    def ultimate_debtor(self):
        """Gets the ultimate_debtor of this RelatedParties.  # noqa: E501

        Ultimate party that owes an amount of money to the (ultimate) creditor.   # noqa: E501

        :return: The ultimate_debtor of this RelatedParties.  # noqa: E501
        :rtype: str
        """
        return self._ultimate_debtor

    @ultimate_debtor.setter
    def ultimate_debtor(self, ultimate_debtor):
        """Sets the ultimate_debtor of this RelatedParties.

        Ultimate party that owes an amount of money to the (ultimate) creditor.   # noqa: E501

        :param ultimate_debtor: The ultimate_debtor of this RelatedParties.  # noqa: E501
        :type: str
        """

        self._ultimate_debtor = ultimate_debtor

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
        if issubclass(RelatedParties, dict):
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
        if not isinstance(other, RelatedParties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

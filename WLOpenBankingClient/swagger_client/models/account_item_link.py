
"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AccountItemLink:
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
        'account_id': 'str',
        'balances': 'Link',
        'transactions': 'Link'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'balances': 'Balances',
        'transactions': 'Transactions'
    }

    def __init__(self, account_id=None, balances=None, transactions=None):  # noqa: E501
        """AccountItemLink - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._balances = None
        self._transactions = None
        self.discriminator = None
        self.account_id = account_id
        if balances is not None:
            self.balances = balances
        if transactions is not None:
            self.transactions = transactions

    @property
    def account_id(self):
        """Gets the account_id of this AccountItemLink.  # noqa: E501

        A unique and immutable identifier used to identify the account resource.   # noqa: E501

        :return: The account_id of this AccountItemLink.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountItemLink.

        A unique and immutable identifier used to identify the account resource.   # noqa: E501

        :param account_id: The account_id of this AccountItemLink.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def balances(self):
        """Gets the balances of this AccountItemLink.  # noqa: E501

        :return: The balances of this AccountItemLink.  # noqa: E501
        :rtype: Link
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this AccountItemLink.

        :param balances: The balances of this AccountItemLink.  # noqa: E501
        :type: Link
        """

        self._balances = balances

    @property
    def transactions(self):
        """Gets the transactions of this AccountItemLink.  # noqa: E501

        :return: The transactions of this AccountItemLink.  # noqa: E501
        :rtype: Link
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this AccountItemLink.

        :param transactions: The transactions of this AccountItemLink.  # noqa: E501
        :type: Link
        """

        self._transactions = transactions

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
        if issubclass(AccountItemLink, dict):
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
        if not isinstance(other, AccountItemLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

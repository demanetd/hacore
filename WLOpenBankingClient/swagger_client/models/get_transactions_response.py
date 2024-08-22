
"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class GetTransactionsResponse:
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
        'date_from': 'datetime',
        'date_to': 'datetime',
        'account_id': 'str',
        'transactions': 'list[Transactions]',
        'links': 'TransactionLinks',
        'metadata': 'Meta'
    }

    attribute_map = {
        'date_from': 'DateFrom',
        'date_to': 'DateTo',
        'account_id': 'AccountId',
        'transactions': 'Transactions',
        'links': 'Links',
        'metadata': 'Metadata'
    }

    def __init__(self, date_from=None, date_to=None, account_id=None, transactions=None, links=None, metadata=None):  # noqa: E501
        """GetTransactionsResponse - a model defined in Swagger"""  # noqa: E501
        self._date_from = None
        self._date_to = None
        self._account_id = None
        self._transactions = None
        self._links = None
        self._metadata = None
        self.discriminator = None
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        self.account_id = account_id
        if transactions is not None:
            self.transactions = transactions
        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata

    @property
    def date_from(self):
        """Gets the date_from of this GetTransactionsResponse.  # noqa: E501

        Date and time. All transactions on this date are included in the result.   # noqa: E501

        :return: The date_from of this GetTransactionsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this GetTransactionsResponse.

        Date and time. All transactions on this date are included in the result.   # noqa: E501

        :param date_from: The date_from of this GetTransactionsResponse.  # noqa: E501
        :type: datetime
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this GetTransactionsResponse.  # noqa: E501

        Date and time, transactions up to this date are included. So transaction on this date are not included in the result.   # noqa: E501

        :return: The date_to of this GetTransactionsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this GetTransactionsResponse.

        Date and time, transactions up to this date are included. So transaction on this date are not included in the result.   # noqa: E501

        :param date_to: The date_to of this GetTransactionsResponse.  # noqa: E501
        :type: datetime
        """

        self._date_to = date_to

    @property
    def account_id(self):
        """Gets the account_id of this GetTransactionsResponse.  # noqa: E501

        Id of the account of the PSU as retrieved form the GET accounts response.   # noqa: E501

        :return: The account_id of this GetTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetTransactionsResponse.

        Id of the account of the PSU as retrieved form the GET accounts response.   # noqa: E501

        :param account_id: The account_id of this GetTransactionsResponse.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def transactions(self):
        """Gets the transactions of this GetTransactionsResponse.  # noqa: E501

        :return: The transactions of this GetTransactionsResponse.  # noqa: E501
        :rtype: list[Transactions]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this GetTransactionsResponse.

        :param transactions: The transactions of this GetTransactionsResponse.  # noqa: E501
        :type: list[Transactions]
        """

        self._transactions = transactions

    @property
    def links(self):
        """Gets the links of this GetTransactionsResponse.  # noqa: E501

        :return: The links of this GetTransactionsResponse.  # noqa: E501
        :rtype: TransactionLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GetTransactionsResponse.

        :param links: The links of this GetTransactionsResponse.  # noqa: E501
        :type: TransactionLinks
        """

        self._links = links

    @property
    def metadata(self):
        """Gets the metadata of this GetTransactionsResponse.  # noqa: E501

        :return: The metadata of this GetTransactionsResponse.  # noqa: E501
        :rtype: Meta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GetTransactionsResponse.

        :param metadata: The metadata of this GetTransactionsResponse.  # noqa: E501
        :type: Meta
        """

        self._metadata = metadata

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
        if issubclass(GetTransactionsResponse, dict):
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
        if not isinstance(other, GetTransactionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Domain:
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
        'domain_code': 'str',
        'family_code': 'str',
        'sub_code': 'str'
    }

    attribute_map = {
        'domain_code': 'DomainCode',
        'family_code': 'FamilyCode',
        'sub_code': 'SubCode'
    }

    def __init__(self, domain_code=None, family_code=None, sub_code=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501
        self._domain_code = None
        self._family_code = None
        self._sub_code = None
        self.discriminator = None
        if domain_code is not None:
            self.domain_code = domain_code
        if family_code is not None:
            self.family_code = family_code
        if sub_code is not None:
            self.sub_code = sub_code

    @property
    def domain_code(self):
        """Gets the domain_code of this Domain.  # noqa: E501

        ExternalBankTransactionDomain1Code.   # noqa: E501

        :return: The domain_code of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._domain_code

    @domain_code.setter
    def domain_code(self, domain_code):
        """Sets the domain_code of this Domain.

        ExternalBankTransactionDomain1Code.   # noqa: E501

        :param domain_code: The domain_code of this Domain.  # noqa: E501
        :type: str
        """

        self._domain_code = domain_code

    @property
    def family_code(self):
        """Gets the family_code of this Domain.  # noqa: E501

        Identify the type of underlying transaction. Specifies the family within a domain.  ExternalBankTransactionFamily1Code.   # noqa: E501

        :return: The family_code of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._family_code

    @family_code.setter
    def family_code(self, family_code):
        """Sets the family_code of this Domain.

        Identify the type of underlying transaction. Specifies the family within a domain.  ExternalBankTransactionFamily1Code.   # noqa: E501

        :param family_code: The family_code of this Domain.  # noqa: E501
        :type: str
        """

        self._family_code = family_code

    @property
    def sub_code(self):
        """Gets the sub_code of this Domain.  # noqa: E501

        Identify the type of underlying transaction. Specifies the sub-product family within a specific family.  ExternalBankTransactionSubFamily1Code.   # noqa: E501

        :return: The sub_code of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._sub_code

    @sub_code.setter
    def sub_code(self, sub_code):
        """Sets the sub_code of this Domain.

        Identify the type of underlying transaction. Specifies the sub-product family within a specific family.  ExternalBankTransactionSubFamily1Code.   # noqa: E501

        :param sub_code: The sub_code of this Domain.  # noqa: E501
        :type: str
        """

        self._sub_code = sub_code

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
        if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

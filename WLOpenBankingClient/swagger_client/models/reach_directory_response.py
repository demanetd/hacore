
"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ReachDirectoryResponse:
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
        'service': 'str',
        'aspsp': 'list[ASPSP]',
        'groups': 'list[Group]'
    }

    attribute_map = {
        'service': 'Service',
        'aspsp': 'ASPSP',
        'groups': 'Groups'
    }

    def __init__(self, service=None, aspsp=None, groups=None):  # noqa: E501
        """ReachDirectoryResponse - a model defined in Swagger"""  # noqa: E501
        self._service = None
        self._aspsp = None
        self._groups = None
        self.discriminator = None
        self.service = service
        self.aspsp = aspsp
        self.groups = groups

    @property
    def service(self):
        """Gets the service of this ReachDirectoryResponse.  # noqa: E501

        The name of the service the ASPSPs are listed for.   # noqa: E501

        :return: The service of this ReachDirectoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ReachDirectoryResponse.

        The name of the service the ASPSPs are listed for.   # noqa: E501

        :param service: The service of this ReachDirectoryResponse.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def aspsp(self):
        """Gets the aspsp of this ReachDirectoryResponse.  # noqa: E501

        :return: The aspsp of this ReachDirectoryResponse.  # noqa: E501
        :rtype: list[ASPSP]
        """
        return self._aspsp

    @aspsp.setter
    def aspsp(self, aspsp):
        """Sets the aspsp of this ReachDirectoryResponse.

        :param aspsp: The aspsp of this ReachDirectoryResponse.  # noqa: E501
        :type: list[ASPSP]
        """
        if aspsp is None:
            raise ValueError("Invalid value for `aspsp`, must not be `None`")  # noqa: E501

        self._aspsp = aspsp

    @property
    def groups(self):
        """Gets the groups of this ReachDirectoryResponse.  # noqa: E501

        A list of ASPSP groups. An ASPSP may belong to one or no group.  # noqa: E501

        :return: The groups of this ReachDirectoryResponse.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ReachDirectoryResponse.

        A list of ASPSP groups. An ASPSP may belong to one or no group.  # noqa: E501

        :param groups: The groups of this ReachDirectoryResponse.  # noqa: E501
        :type: list[Group]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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
        if issubclass(ReachDirectoryResponse, dict):
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
        if not isinstance(other, ReachDirectoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

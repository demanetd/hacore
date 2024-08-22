
"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RefundAuthorisationApproachLinks:
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
        'pre_authentication_for_embedded': 'Link',
        'redirect_url': 'Link',
        'post_authorisation_for_explicit': 'Link',
        'post_identification_for_decoupled': 'Link',
        'post_authorisation_for_embedded': 'Link',
        'select_authentication_method': 'Link',
        'authorize_transaction': 'Link',
        'confirmation_required': 'Link',
        'get_refund_status': 'Link'
    }

    attribute_map = {
        'pre_authentication_for_embedded': 'PreAuthenticationForEmbedded',
        'redirect_url': 'RedirectUrl',
        'post_authorisation_for_explicit': 'PostAuthorisationForExplicit',
        'post_identification_for_decoupled': 'PostIdentificationForDecoupled',
        'post_authorisation_for_embedded': 'PostAuthorisationForEmbedded',
        'select_authentication_method': 'SelectAuthenticationMethod',
        'authorize_transaction': 'AuthorizeTransaction',
        'confirmation_required': 'ConfirmationRequired',
        'get_refund_status': 'GetRefundStatus'
    }

    def __init__(self, pre_authentication_for_embedded=None, redirect_url=None, post_authorisation_for_explicit=None, post_identification_for_decoupled=None, post_authorisation_for_embedded=None, select_authentication_method=None, authorize_transaction=None, confirmation_required=None, get_refund_status=None):  # noqa: E501
        """RefundAuthorisationApproachLinks - a model defined in Swagger"""  # noqa: E501
        self._pre_authentication_for_embedded = None
        self._redirect_url = None
        self._post_authorisation_for_explicit = None
        self._post_identification_for_decoupled = None
        self._post_authorisation_for_embedded = None
        self._select_authentication_method = None
        self._authorize_transaction = None
        self._confirmation_required = None
        self._get_refund_status = None
        self.discriminator = None
        if pre_authentication_for_embedded is not None:
            self.pre_authentication_for_embedded = pre_authentication_for_embedded
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if post_authorisation_for_explicit is not None:
            self.post_authorisation_for_explicit = post_authorisation_for_explicit
        if post_identification_for_decoupled is not None:
            self.post_identification_for_decoupled = post_identification_for_decoupled
        if post_authorisation_for_embedded is not None:
            self.post_authorisation_for_embedded = post_authorisation_for_embedded
        if select_authentication_method is not None:
            self.select_authentication_method = select_authentication_method
        if authorize_transaction is not None:
            self.authorize_transaction = authorize_transaction
        if confirmation_required is not None:
            self.confirmation_required = confirmation_required
        if get_refund_status is not None:
            self.get_refund_status = get_refund_status

    @property
    def pre_authentication_for_embedded(self):
        """Gets the pre_authentication_for_embedded of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The pre_authentication_for_embedded of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._pre_authentication_for_embedded

    @pre_authentication_for_embedded.setter
    def pre_authentication_for_embedded(self, pre_authentication_for_embedded):
        """Sets the pre_authentication_for_embedded of this RefundAuthorisationApproachLinks.

        :param pre_authentication_for_embedded: The pre_authentication_for_embedded of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._pre_authentication_for_embedded = pre_authentication_for_embedded

    @property
    def redirect_url(self):
        """Gets the redirect_url of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The redirect_url of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this RefundAuthorisationApproachLinks.

        :param redirect_url: The redirect_url of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._redirect_url = redirect_url

    @property
    def post_authorisation_for_explicit(self):
        """Gets the post_authorisation_for_explicit of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The post_authorisation_for_explicit of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._post_authorisation_for_explicit

    @post_authorisation_for_explicit.setter
    def post_authorisation_for_explicit(self, post_authorisation_for_explicit):
        """Sets the post_authorisation_for_explicit of this RefundAuthorisationApproachLinks.

        :param post_authorisation_for_explicit: The post_authorisation_for_explicit of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._post_authorisation_for_explicit = post_authorisation_for_explicit

    @property
    def post_identification_for_decoupled(self):
        """Gets the post_identification_for_decoupled of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The post_identification_for_decoupled of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._post_identification_for_decoupled

    @post_identification_for_decoupled.setter
    def post_identification_for_decoupled(self, post_identification_for_decoupled):
        """Sets the post_identification_for_decoupled of this RefundAuthorisationApproachLinks.

        :param post_identification_for_decoupled: The post_identification_for_decoupled of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._post_identification_for_decoupled = post_identification_for_decoupled

    @property
    def post_authorisation_for_embedded(self):
        """Gets the post_authorisation_for_embedded of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The post_authorisation_for_embedded of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._post_authorisation_for_embedded

    @post_authorisation_for_embedded.setter
    def post_authorisation_for_embedded(self, post_authorisation_for_embedded):
        """Sets the post_authorisation_for_embedded of this RefundAuthorisationApproachLinks.

        :param post_authorisation_for_embedded: The post_authorisation_for_embedded of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._post_authorisation_for_embedded = post_authorisation_for_embedded

    @property
    def select_authentication_method(self):
        """Gets the select_authentication_method of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The select_authentication_method of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._select_authentication_method

    @select_authentication_method.setter
    def select_authentication_method(self, select_authentication_method):
        """Sets the select_authentication_method of this RefundAuthorisationApproachLinks.

        :param select_authentication_method: The select_authentication_method of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._select_authentication_method = select_authentication_method

    @property
    def authorize_transaction(self):
        """Gets the authorize_transaction of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The authorize_transaction of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._authorize_transaction

    @authorize_transaction.setter
    def authorize_transaction(self, authorize_transaction):
        """Sets the authorize_transaction of this RefundAuthorisationApproachLinks.

        :param authorize_transaction: The authorize_transaction of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._authorize_transaction = authorize_transaction

    @property
    def confirmation_required(self):
        """Gets the confirmation_required of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The confirmation_required of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._confirmation_required

    @confirmation_required.setter
    def confirmation_required(self, confirmation_required):
        """Sets the confirmation_required of this RefundAuthorisationApproachLinks.

        :param confirmation_required: The confirmation_required of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._confirmation_required = confirmation_required

    @property
    def get_refund_status(self):
        """Gets the get_refund_status of this RefundAuthorisationApproachLinks.  # noqa: E501

        :return: The get_refund_status of this RefundAuthorisationApproachLinks.  # noqa: E501
        :rtype: Link
        """
        return self._get_refund_status

    @get_refund_status.setter
    def get_refund_status(self, get_refund_status):
        """Sets the get_refund_status of this RefundAuthorisationApproachLinks.

        :param get_refund_status: The get_refund_status of this RefundAuthorisationApproachLinks.  # noqa: E501
        :type: Link
        """

        self._get_refund_status = get_refund_status

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
        if issubclass(RefundAuthorisationApproachLinks, dict):
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
        if not isinstance(other, RefundAuthorisationApproachLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

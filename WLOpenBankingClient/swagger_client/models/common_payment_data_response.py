
"""Open Banking Reach + AIS  PIS

# REACH The Reach Directory is used to get the a list of ASPSP's which can be reached for a  specific Service. **Sandbox** The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire) 97fb13a74c712d8c7a50476e71769eaf  # AIS There are several possible flows (sequence of API calls) to obtain a consent before Account Information data can be retrieved. Which API's are required depend on the ASPSP (the bank of the PSU) and the chosen strong customer authentication approach. The response of an API call will indicate in the Links section which next API call is required to complete the consent request.  **Sandbox** Several AspspId's are available to test specific account information scenario's, see sandbox     documentation. The following authorization token can be used to test in the sandbox (unlike a real token this one     doesn't expire) **d5bd895a4080dbbb469a207460b6fca**  # PIS There are several flows (sequence of API calls) to complete a payment. Which API's are required depend on the choosen `PaymentProduct`, ASPSP (debtor bank) and the chosen strong customer authentication approach. The response of an API call will indicate in the 'Links' section which next API call is required to complete the payment. Both PSD2 and IDEAL payments are supported. **Sandbox** Several AspspId's are available to test specific PSD2 payment initiation scenario's, see sandbox documentation.  The following authorization token can be used to test in the sandbox (unlike a real token this one doesn't expire): **97fb13a74c712d8c7a50476e71769eaf**   # noqa: E501

OpenAPI spec version: 3.2.0 + 3.6.0 + 3.7.0
    
Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CommonPaymentDataResponse:
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
        'expiry_date_timestamp': 'datetime',
        'guaranteed_amount': 'str',
        'payment_status': 'PaymentStatusEnum',
        'payment_id': 'str',
        'aspsp_payment_id': 'str',
        'aspsp_id': 'str',
        'initiating_party_reference_id': 'str',
        'funds_available': 'bool',
        'debtor_information': 'DebtorInformationResponse',
        'amount_related_details': 'AmountRelatedDetails',
        'authorisation_required_data': 'AuthorisationRequiredData',
        'psu_message': 'str'
    }

    attribute_map = {
        'expiry_date_timestamp': 'ExpiryDateTimestamp',
        'guaranteed_amount': 'GuaranteedAmount',
        'payment_status': 'PaymentStatus',
        'payment_id': 'PaymentId',
        'aspsp_payment_id': 'AspspPaymentId',
        'aspsp_id': 'AspspId',
        'initiating_party_reference_id': 'InitiatingPartyReferenceId',
        'funds_available': 'FundsAvailable',
        'debtor_information': 'DebtorInformation',
        'amount_related_details': 'AmountRelatedDetails',
        'authorisation_required_data': 'AuthorisationRequiredData',
        'psu_message': 'PsuMessage'
    }

    def __init__(self, expiry_date_timestamp=None, guaranteed_amount=None, payment_status=None, payment_id=None, aspsp_payment_id=None, aspsp_id=None, initiating_party_reference_id=None, funds_available=None, debtor_information=None, amount_related_details=None, authorisation_required_data=None, psu_message=None):  # noqa: E501
        """CommonPaymentDataResponse - a model defined in Swagger"""  # noqa: E501
        self._expiry_date_timestamp = None
        self._guaranteed_amount = None
        self._payment_status = None
        self._payment_id = None
        self._aspsp_payment_id = None
        self._aspsp_id = None
        self._initiating_party_reference_id = None
        self._funds_available = None
        self._debtor_information = None
        self._amount_related_details = None
        self._authorisation_required_data = None
        self._psu_message = None
        self.discriminator = None
        if expiry_date_timestamp is not None:
            self.expiry_date_timestamp = expiry_date_timestamp
        if guaranteed_amount is not None:
            self.guaranteed_amount = guaranteed_amount
        self.payment_status = payment_status
        self.payment_id = payment_id
        if aspsp_payment_id is not None:
            self.aspsp_payment_id = aspsp_payment_id
        if aspsp_id is not None:
            self.aspsp_id = aspsp_id
        if initiating_party_reference_id is not None:
            self.initiating_party_reference_id = initiating_party_reference_id
        if funds_available is not None:
            self.funds_available = funds_available
        if debtor_information is not None:
            self.debtor_information = debtor_information
        if amount_related_details is not None:
            self.amount_related_details = amount_related_details
        if authorisation_required_data is not None:
            self.authorisation_required_data = authorisation_required_data
        if psu_message is not None:
            self.psu_message = psu_message

    @property
    def expiry_date_timestamp(self):
        """Gets the expiry_date_timestamp of this CommonPaymentDataResponse.  # noqa: E501

        The timestamp from which the transaction operation will expire, expressed in UTC time format(YYYY-MM-DDThh:mm:ss.sssZ)   # noqa: E501

        :return: The expiry_date_timestamp of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date_timestamp

    @expiry_date_timestamp.setter
    def expiry_date_timestamp(self, expiry_date_timestamp):
        """Sets the expiry_date_timestamp of this CommonPaymentDataResponse.

        The timestamp from which the transaction operation will expire, expressed in UTC time format(YYYY-MM-DDThh:mm:ss.sssZ)   # noqa: E501

        :param expiry_date_timestamp: The expiry_date_timestamp of this CommonPaymentDataResponse.  # noqa: E501
        :type: datetime
        """

        self._expiry_date_timestamp = expiry_date_timestamp

    @property
    def guaranteed_amount(self):
        """Gets the guaranteed_amount of this CommonPaymentDataResponse.  # noqa: E501

        The amount guaranteed by the ASPSP/Issuer to the Merchant/CPSP. Will be provided if the min max amount values are defined in the request   # noqa: E501

        :return: The guaranteed_amount of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._guaranteed_amount

    @guaranteed_amount.setter
    def guaranteed_amount(self, guaranteed_amount):
        """Sets the guaranteed_amount of this CommonPaymentDataResponse.

        The amount guaranteed by the ASPSP/Issuer to the Merchant/CPSP. Will be provided if the min max amount values are defined in the request   # noqa: E501

        :param guaranteed_amount: The guaranteed_amount of this CommonPaymentDataResponse.  # noqa: E501
        :type: str
        """

        self._guaranteed_amount = guaranteed_amount

    @property
    def payment_status(self):
        """Gets the payment_status of this CommonPaymentDataResponse.  # noqa: E501

        :return: The payment_status of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: PaymentStatusEnum
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this CommonPaymentDataResponse.

        :param payment_status: The payment_status of this CommonPaymentDataResponse.  # noqa: E501
        :type: PaymentStatusEnum
        """
        if payment_status is None:
            raise ValueError("Invalid value for `payment_status`, must not be `None`")  # noqa: E501

        self._payment_status = payment_status

    @property
    def payment_id(self):
        """Gets the payment_id of this CommonPaymentDataResponse.  # noqa: E501

        Id generated by the Open Banking Service. This should be used to refer to this payment in subsequent api calls.   # noqa: E501

        :return: The payment_id of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this CommonPaymentDataResponse.

        Id generated by the Open Banking Service. This should be used to refer to this payment in subsequent api calls.   # noqa: E501

        :param payment_id: The payment_id of this CommonPaymentDataResponse.  # noqa: E501
        :type: str
        """
        if payment_id is None:
            raise ValueError("Invalid value for `payment_id`, must not be `None`")  # noqa: E501

        self._payment_id = payment_id

    @property
    def aspsp_payment_id(self):
        """Gets the aspsp_payment_id of this CommonPaymentDataResponse.  # noqa: E501

        Id used by the ASPSP/iDEAL Hub to refer to the payment.   # noqa: E501

        :return: The aspsp_payment_id of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._aspsp_payment_id

    @aspsp_payment_id.setter
    def aspsp_payment_id(self, aspsp_payment_id):
        """Sets the aspsp_payment_id of this CommonPaymentDataResponse.

        Id used by the ASPSP/iDEAL Hub to refer to the payment.   # noqa: E501

        :param aspsp_payment_id: The aspsp_payment_id of this CommonPaymentDataResponse.  # noqa: E501
        :type: str
        """

        self._aspsp_payment_id = aspsp_payment_id

    @property
    def aspsp_id(self):
        """Gets the aspsp_id of this CommonPaymentDataResponse.  # noqa: E501

        Id of the ASPSP selected by the PSU.   # noqa: E501

        :return: The aspsp_id of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._aspsp_id

    @aspsp_id.setter
    def aspsp_id(self, aspsp_id):
        """Sets the aspsp_id of this CommonPaymentDataResponse.

        Id of the ASPSP selected by the PSU.   # noqa: E501

        :param aspsp_id: The aspsp_id of this CommonPaymentDataResponse.  # noqa: E501
        :type: str
        """

        self._aspsp_id = aspsp_id

    @property
    def initiating_party_reference_id(self):
        """Gets the initiating_party_reference_id of this CommonPaymentDataResponse.  # noqa: E501

        Reference to the payment created by the Initiating Party. This Id will not be visible to the Payment Service User.   # noqa: E501

        :return: The initiating_party_reference_id of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._initiating_party_reference_id

    @initiating_party_reference_id.setter
    def initiating_party_reference_id(self, initiating_party_reference_id):
        """Sets the initiating_party_reference_id of this CommonPaymentDataResponse.

        Reference to the payment created by the Initiating Party. This Id will not be visible to the Payment Service User.   # noqa: E501

        :param initiating_party_reference_id: The initiating_party_reference_id of this CommonPaymentDataResponse.  # noqa: E501
        :type: str
        """

        self._initiating_party_reference_id = initiating_party_reference_id

    @property
    def funds_available(self):
        """Gets the funds_available of this CommonPaymentDataResponse.  # noqa: E501

        Information whether sufficient funding is available.   # noqa: E501

        :return: The funds_available of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: bool
        """
        return self._funds_available

    @funds_available.setter
    def funds_available(self, funds_available):
        """Sets the funds_available of this CommonPaymentDataResponse.

        Information whether sufficient funding is available.   # noqa: E501

        :param funds_available: The funds_available of this CommonPaymentDataResponse.  # noqa: E501
        :type: bool
        """

        self._funds_available = funds_available

    @property
    def debtor_information(self):
        """Gets the debtor_information of this CommonPaymentDataResponse.  # noqa: E501

        :return: The debtor_information of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: DebtorInformationResponse
        """
        return self._debtor_information

    @debtor_information.setter
    def debtor_information(self, debtor_information):
        """Sets the debtor_information of this CommonPaymentDataResponse.

        :param debtor_information: The debtor_information of this CommonPaymentDataResponse.  # noqa: E501
        :type: DebtorInformationResponse
        """

        self._debtor_information = debtor_information

    @property
    def amount_related_details(self):
        """Gets the amount_related_details of this CommonPaymentDataResponse.  # noqa: E501

        :return: The amount_related_details of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: AmountRelatedDetails
        """
        return self._amount_related_details

    @amount_related_details.setter
    def amount_related_details(self, amount_related_details):
        """Sets the amount_related_details of this CommonPaymentDataResponse.

        :param amount_related_details: The amount_related_details of this CommonPaymentDataResponse.  # noqa: E501
        :type: AmountRelatedDetails
        """

        self._amount_related_details = amount_related_details

    @property
    def authorisation_required_data(self):
        """Gets the authorisation_required_data of this CommonPaymentDataResponse.  # noqa: E501

        :return: The authorisation_required_data of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: AuthorisationRequiredData
        """
        return self._authorisation_required_data

    @authorisation_required_data.setter
    def authorisation_required_data(self, authorisation_required_data):
        """Sets the authorisation_required_data of this CommonPaymentDataResponse.

        :param authorisation_required_data: The authorisation_required_data of this CommonPaymentDataResponse.  # noqa: E501
        :type: AuthorisationRequiredData
        """

        self._authorisation_required_data = authorisation_required_data

    @property
    def psu_message(self):
        """Gets the psu_message of this CommonPaymentDataResponse.  # noqa: E501

        Text to be displayed to the PSU.   # noqa: E501

        :return: The psu_message of this CommonPaymentDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._psu_message

    @psu_message.setter
    def psu_message(self, psu_message):
        """Sets the psu_message of this CommonPaymentDataResponse.

        Text to be displayed to the PSU.   # noqa: E501

        :param psu_message: The psu_message of this CommonPaymentDataResponse.  # noqa: E501
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
        if issubclass(CommonPaymentDataResponse, dict):
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
        if not isinstance(other, CommonPaymentDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

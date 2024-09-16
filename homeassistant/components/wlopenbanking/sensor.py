"""Support for balance data via the Worldline Openbanking API."""

from __future__ import annotations

import datetime
from datetime import timedelta
import logging
import sys

import requests
import voluptuous as vol

sys.path.insert(0, "/workspaces/hacore/WLOpenBankingClient")

import uuid

import swagger_client
from swagger_client.rest import ApiException

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA as SENSOR_PLATFORM_SCHEMA,
    SensorEntity,
)
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_NAME
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)

BALANCE_TYPES = ["cleared_balance", "effective_balance"]

CONF_ACCOUNTS = "accounts"
CONF_BALANCE_TYPES = "balance_types"
CONF_SANDBOX = "sandbox"

DEFAULT_SANDBOX = False
DEFAULT_ACCOUNT_NAME = "123456"


SCAN_INTERVAL = timedelta(seconds=180)

ACCOUNT_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ACCESS_TOKEN): cv.string,
        vol.Optional(CONF_BALANCE_TYPES, default=BALANCE_TYPES): vol.All(
            cv.ensure_list, [vol.In(BALANCE_TYPES)]
        ),
        vol.Optional(CONF_NAME, default=DEFAULT_ACCOUNT_NAME): cv.string,
        vol.Optional(CONF_SANDBOX, default=DEFAULT_SANDBOX): cv.boolean,
    }
)

PLATFORM_SCHEMA = SENSOR_PLATFORM_SCHEMA.extend(
    {vol.Required(CONF_ACCOUNTS): vol.Schema([ACCOUNT_SCHEMA])}
)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_devices: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Sterling Bank sensor platform."""

    sensors: list[WlOpenBankingBalanceSensor] = []
    for account in config[CONF_ACCOUNTS]:
        try:
            wlOpenBanking_account = None
            # wlOpenBanking_account = WlOpenBankingAccount(
            #     account[CONF_ACCESS_TOKEN], sandbox=account[CONF_SANDBOX]
            # )
            sensors.extend(
                WlOpenBankingBalanceSensor(
                    wlOpenBanking_account, account[CONF_NAME], balance_type
                )
                for balance_type in account[CONF_BALANCE_TYPES]
            )
        except requests.exceptions.HTTPError as error:
            _LOGGER.error(
                "Unable to set up WlOpenBanking account '%s': %s",
                account[CONF_NAME],
                error,
            )

    add_devices(sensors, True)


class WlOpenBankingBalanceSensor(SensorEntity):
    """Representation of a WlOpenBanking balance sensor."""

    _attr_icon = "mdi:currency-gbp"

    def __init__(self, wlOpenBanking_account, account_name, balance_data_type):
        """Initialize the sensor."""
        self._wlOpenBanking_account = wlOpenBanking_account
        self._balance_data_type = balance_data_type
        self._state = None
        self._account_name = account_name

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{} {}".format(
            self._account_name, self._balance_data_type.replace("_", " ").capitalize()
        )

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement."""
        # return self._wlOpenBanking_account.currency
        return "EUR"

    def update(self) -> None:
        """Fetch new state data for the sensor."""
        # self._wlOpenBanking_account.update_balance_data()
        configuration = swagger_client.Configuration()
        configuration.debug = True
        api_client = swagger_client.ApiClient(configuration)
        api_client.set_default_header(
            "Authorization", "Bearer d5bd895a4080dbbb469a207460b6fca"
        )
        api_instance = swagger_client.AccountInformationServiceApi(api_client)
        try:
            # Requests by user id
            xreqid = str(uuid.uuid4())
            psuid = "123456"
            consentid = "1126608"
            aspspid = "20116"
            accountid = "182794"
            api_response = api_instance.balances(
                psuid, aspspid, accountid, xreqid, datetime.datetime.now()
            )
        except ApiException as e:
            print(
                "Exception when calling AccountInformationServiceApi.consent_extended: %s\n"
                % e
            )

        if self._balance_data_type == "cleared_balance":
            self._state = api_response.balances[0].amount
        elif self._balance_data_type == "effective_balance":
            self._state = api_response.balances[1].amount

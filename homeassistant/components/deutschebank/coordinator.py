"""The Deutsche Bank integration."""

from dataclasses import dataclass
from datetime import timedelta
import logging
from typing import Any

from monzopy import AuthorisationExpiredError

from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .api import AuthenticatedDeutscheBankAPI
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


@dataclass
class DeutscheBankData:
    """A dataclass for holding sensor data returned by the DataUpdateCoordinator."""

    accounts: list[dict[str, Any]]


class DeutscheBankCoordinator(DataUpdateCoordinator[DeutscheBankData]):
    """Class to manage fetching Monzo data from the API."""

    def __init__(self, hass: HomeAssistant, api: AuthenticatedDeutscheBankAPI) -> None:
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
        )
        self.api = api

    async def _async_update_data(self) -> DeutscheBankData:
        """Fetch data from Deutsche Bank API."""
        try:
            accounts = await self.api.user_account.accounts()
        except AuthorisationExpiredError as err:
            raise ConfigEntryAuthFailed from err

        return DeutscheBankData(accounts)

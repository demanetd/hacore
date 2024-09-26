"""API for Deutsche Bank bound to Home Assistant OAuth."""

from aiohttp import ClientSession

from homeassistant.helpers import config_entry_oauth2_flow

from .deutschebankpy import AbstractDeutscheBankApi


class AuthenticatedDeutscheBankAPI(AbstractDeutscheBankApi):
    """A Deutsche Bank API instance with authentication tied to an OAuth2 based config entry."""

    def __init__(
        self,
        websession: ClientSession,
        oauth_session: config_entry_oauth2_flow.OAuth2Session,
    ) -> None:
        """Initialize Deutsche Bank auth."""
        super().__init__(websession)
        self._oauth_session = oauth_session

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
        if not self._oauth_session.valid_token:
            await self._oauth_session.async_ensure_token_valid()

        return str(self._oauth_session.token["access_token"])

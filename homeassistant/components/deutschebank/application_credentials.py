"""application_credentials platform the Deutsche Bank integration."""

from homeassistant.components.application_credentials import AuthorizationServer
from homeassistant.core import HomeAssistant

OAUTH2_AUTHORIZE = "https://simulator-api.db.com:443/gw/oidc/authorize"
OAUTH2_TOKEN = "https://simulator-api.db.com:443/gw/oidc/token"


async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer:
    """Return authorization server."""
    return AuthorizationServer(
        authorize_url=OAUTH2_AUTHORIZE,
        token_url=OAUTH2_TOKEN,
    )

"""API for Deutsche Bank."""

from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable
from typing import Any
from urllib.parse import urlparse

from aiohttp import ClientSession

API_URL_BASE = "https://simulator-api.db.com:443/gw/dbapi/banking/"


class AbstractDeutscheBankApi(ABC):  # pylint: disable=too-few-public-methods
    """An abstract class for accessing the Deutsche Bank API."""

    def __init__(self, session: ClientSession) -> None:
        """Initialize.

        Args:
            api_key: An API key.
            session: An optional aiohttp ClientSession.

        """
        self._session: ClientSession = session
        self.user_account = UserAccount(self._request)

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def _request(
        self,
        method: str,
        endpoint: str,
        *,
        base_url: str = API_URL_BASE,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        access_token = await self.async_get_access_token()
        headers["Authorization"] = f"Bearer {access_token}"

        async with self._session.request(
            method,
            f"{base_url}/{endpoint}",
            **kwargs,
            headers=headers,
        ) as resp:
            data = await resp.json(content_type=None)

        try:
            data_dict: dict[str, Any] = dict(data)
        except ValueError:
            raise InvalidDeutscheBankAPIResponseError from ValueError

        return data_dict


INVALID_ACCOUNT_TYPES = ["no_invalid"]

CURRENT_ACCOUNT = "CURRENT_ACCOUNT"

ACCOUNT_NAMES = {CURRENT_ACCOUNT: "Current Account"}

TOKEN_EXPIRY_CODE = "unauthorized.bad_access_token.expired"
CODE = "code"


class UserAccount:
    """Define an object representing a Monzo account holder."""

    def __init__(self, request: Callable[..., Awaitable[dict[str, Any]]]) -> None:
        """Initialise the account."""
        self._request: Callable[..., Awaitable[dict[str, Any]]] = request
        self._account_ids: set[str] = set()
        self._webhook_ids: list[str] = []

    async def accounts(self) -> list[dict[str, Any]]:
        """List accounts and their balances."""
        result = []

        accounts = await self._get_accounts()
        for account in accounts:
            try:
                if account["accountType"] not in INVALID_ACCOUNT_TYPES:
                    transactions = await self._get_transactions(
                        account["iban"], "2020-01-01"
                    )
                    ibanAmounts: dict[str, Any] = {}
                    for trn in transactions:
                        try:
                            ibanAmounts[trn["counterPartyIban"]] += trn["amount"]
                        except KeyError:
                            ibanAmounts[trn["counterPartyIban"]] = trn["amount"]
                    result.append(
                        {
                            "id": account["iban"],
                            "name": account["productDescription"],
                            "type": account["accountType"],
                            "balance": account["currentBalance"],
                            "currency": account["currencyCode"],
                            "ibanAmounts": ibanAmounts,
                        }
                    )
            except KeyError:
                raise InvalidDeutscheBankAPIResponseError from KeyError

        return result

    async def _get_accounts(self) -> list[dict[str, Any]]:
        res = await self._request("get", "cashAccounts/v2/")
        valid_accounts = []
        try:
            for acc in res["accounts"]:
                if acc["accountType"] not in INVALID_ACCOUNT_TYPES:
                    self._account_ids.add(acc["iban"])
                    valid_accounts.append(acc)
        except KeyError:
            await _raise_auth_or_response_error(res)
        return valid_accounts

    async def _get_transactions(
        self, ibanAccount: str, bookinDateFrom: str
    ) -> list[dict[str, Any]]:
        params = {
            "iban": ibanAccount,
            "sortBy": "bookingDate[DESC]",
            "bookinDateFrom": bookinDateFrom,
        }
        res = await self._request("get", "transactions/v2/", params=params)
        valid_transactions = []
        try:
            for trn in res["transactions"]:
                try:
                    if trn["counterPartyIban"] != "":
                        # self._account_ids.add(acc["iban"])
                        valid_transactions.append(trn)
                except KeyError:
                    # just ignore if no counterPartyIban
                    pass
        except KeyError:
            await _raise_auth_or_response_error(res)
        return valid_transactions

    async def register_webhooks(self, webhook_url: str) -> None:
        """Register webhooks for all bank accounts."""
        if not self._account_ids:
            await self._get_accounts()
        for account_id in self._account_ids:
            res = await self._request(
                "post", "webhooks", data={"account_id": account_id, "url": webhook_url}
            )
            try:
                self._webhook_ids.append(res["webhook"]["id"])
            except KeyError:
                raise InvalidDeutscheBankAPIResponseError from KeyError

    async def list_webhooks(self, host: str | None = None) -> list[str]:
        """List all webhooks registered on the account, optionally filtering by host."""
        if host:
            host = urlparse(host).hostname
        if not self._account_ids:
            await self._get_accounts()
        webhook_ids = []
        for account_id in self._account_ids:
            res = await self._request(
                "get", "webhooks", params={"account_id": account_id}
            )
            try:
                # for webhook in res["webhooks"]:
                #    if not host or host == urlparse(webhook["url"]).hostname:
                #        webhook_ids.append(webhook["id"])
                webhook_ids.extend(
                    webhook
                    for webhook in res["webhooks"]
                    if not host or host == urlparse(webhook["url"]).hostname
                )
            except KeyError:
                raise InvalidDeutscheBankAPIResponseError from KeyError
        return webhook_ids

    async def unregister_webhooks(self, host: str | None = None) -> None:
        """Unregister all webhooks, optionally filtering by host."""
        for webhook_id in await self.list_webhooks(host):
            await self._request("delete", f"webhooks/{webhook_id}")


async def _authorisation_expired(response: dict[str, Any]) -> bool:
    return CODE in response and response[CODE] == TOKEN_EXPIRY_CODE


async def _raise_auth_or_response_error(response: dict[str, Any]) -> None:
    if _authorisation_expired(response):
        raise AuthorisationExpiredError
    raise InvalidDeutscheBankAPIResponseError


class InvalidDeutscheBankAPIResponseError(Exception):
    """Error thrown when the external Monzo API returns an invalid response."""

    def __init__(self, *args: object) -> None:
        """Initialise error."""
        super().__init__(*args)


class AuthorisationExpiredError(Exception):
    """Error thrown when the external Monzo API authentication has expired."""

    def __init__(self, *args: object) -> None:
        """Initialise error."""
        super().__init__(*args)

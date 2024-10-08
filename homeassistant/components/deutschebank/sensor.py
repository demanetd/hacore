"""Platform for sensor integration."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pprint import pprint
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import DeutscheBankCoordinator
from .const import DOMAIN
from .coordinator import DeutscheBankData
from .entity import DeutscheBankBaseEntity


@dataclass(frozen=True, kw_only=True)
class DeutscheBankSensorEntityDescription(SensorEntityDescription):
    """Describes Deutsche Bank sensor entity."""

    value_fn: Callable[[dict[str, Any]], StateType]


ACCOUNT_SENSORS = (
    DeutscheBankSensorEntityDescription(
        key="balance",
        translation_key="balance",
        value_fn=lambda data: data["balance"],
        device_class=SensorDeviceClass.MONETARY,
        native_unit_of_measurement="EUR",
        suggested_display_precision=2,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Defer sensor setup to the shared sensor module."""
    coordinator: DeutscheBankCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    pprint(coordinator.data.accounts)
    accounts = [
        DeutscheBankSensor(
            coordinator,
            entity_description,
            index,
            account["name"],
            lambda x: x.accounts,
            {trn["counterPartyIban"]: trn["amount"] for trn in account["transactions"]},
        )
        for entity_description in ACCOUNT_SENSORS
        for index, account in enumerate(coordinator.data.accounts)
    ]
    pprint(accounts)

    async_add_entities(accounts)


class DeutscheBankSensor(DeutscheBankBaseEntity, SensorEntity):
    """Represents a Deutsche Bank sensor."""

    entity_description: DeutscheBankSensorEntityDescription

    def __init__(
        self,
        coordinator: DeutscheBankCoordinator,
        entity_description: DeutscheBankSensorEntityDescription,
        index: int,
        device_model: str,
        data_accessor: Callable[[DeutscheBankData], list[dict[str, Any]]],
        _attributes: dict[str, Any],
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, index, device_model, data_accessor)
        self.entity_description = entity_description
        self._attr_unique_id = f"{self.data['id']}_{entity_description.key}"
        self._attributes = _attributes

    @property
    def native_value(self) -> StateType:
        """Return the state."""

        try:
            state = self.entity_description.value_fn(self.data)
            pprint(state)  # noqa: T203
        except (KeyError, ValueError):
            return None

        return state

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return attributes for the sensor."""
        return self._attributes

import abc
from typing import Any, Dict, Final, Optional, Tuple
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..sensor import Sensor


class PowerSensor(Sensor):
    """PowerSensor reports information about voltage, current and power.

    This acts as an abstract base class for any sensors that can provide data regarding voltage, current and/or power.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "power_sensor")

    @abc.abstractmethod
    async def get_voltage(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Get the voltage reading and bool IsAC

        Returns:
            Tuple[float, bool]: voltage (volts) and bool IsAC
        """
        ...

    @abc.abstractmethod
    async def get_current(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Tuple[float, bool]:
        """Get the current reading and bool IsAC

        Returns:
            Tuple[float, bool]: current (amperes) and bool IsAC
        """
        ...

    @abc.abstractmethod
    async def get_power(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
        """Get the power reading in watts

        Returns:
            float: power in watts
        """
        ...
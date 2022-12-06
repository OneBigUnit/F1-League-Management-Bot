from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING

import nextcord

if TYPE_CHECKING:
    from .driver import Driver


class Constructor:
    DEFAULT_DESCRIPTION = ""

    def __init__(self, name: str, team_colour: nextcord.Colour, description: Optional[str] = None) -> None:
        self.name = name
        self.team_colour = team_colour
        self.description = self.__class__.DEFAULT_DESCRIPTION if description is None else description
        self.drivers: List[Driver] = []
        self.points: int = 0

    def __str__(self) -> str:
        return self.name

    def sign(self, *drivers: Driver) -> None:
        for driver in drivers:
            self.drivers.append(driver)
            driver.constructor = self

    def discharge(self, *drivers: Driver) -> None:
        for driver in drivers:
            self.drivers.remove(driver)
            driver.constructor = None

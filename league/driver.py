from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .league import Constructor


class Driver:
    def __init__(self, first_name: str, last_name: str, default_constructor: Optional[Constructor] = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.constructor = default_constructor
        self.points: int = 0

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

from typing import Optional

import nextcord

from . import Driver


class Contestant(Driver):
    def __init__(self, first_name: str, last_name: str,
                 discord_member: nextcord.Member, display_name: Optional[str] = None) -> None:
        super().__init__(first_name, last_name)
        self.discord_member = discord_member
        self._display_name = display_name

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}" if self._display_name is None else self._display_name

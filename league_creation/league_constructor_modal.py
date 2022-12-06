from typing import Callable, Awaitable

import nextcord

from league import League, Constructors
from league_creation import LeagueConstructorModal


class LeagueConstructorModal(nextcord.ui.Modal):
    CONSTRUCTOR_OPTIONS = {
        **{nextcord.SelectOption(label=str(constructor.value)): constructor.value for constructor in Constructors},
        **{nextcord.SelectOption(label="Custom Constructor"): None}
    }

    def __init__(self, callback: Callable[[nextcord.Interaction, League], Awaitable[None]], league: League,
                 ) -> None:
        super().__init__("", timeout=None)
        self.league = league
        self.on_submit = callback

        self.name = nextcord.ui.TextInput(
            label="Constructor Name",
            placeholder="Enter your constructor's name here...",
            min_length=3,
            max_length=50,
        )
        self.add_item(self.name)

        self.colour = nextcord.ui.TextInput(
            label="Constructor Colour",
            placeholder="Enter your constructor's team colour here (RR-GG-BB)...",
            min_length=7,
            max_length=7,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="Constructor Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Enter your constructor's description here...",
            required=False,
            max_length=4_000,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.league.add_constructors()
        await self.on_submit(interaction, self.league)

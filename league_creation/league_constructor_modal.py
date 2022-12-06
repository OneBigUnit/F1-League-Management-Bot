from typing import Callable, Awaitable

import nextcord

from league import League, Constructors


class LeagueConstructorModal(nextcord.ui.Modal):
    CONSTRUCTOR_OPTIONS = {
        **{nextcord.SelectOption(label=str(constructor.value)): constructor.value for constructor in Constructors},
        **{nextcord.SelectOption(label="Custom Constructor"): None}
    }

    def __init__(self, callback: Callable[[nextcord.Interaction, League], Awaitable[None]], league: League,
                 number_of_teams: int) -> None:
        super().__init__("", timeout=None)
        self.league = league
        self.on_submit = callback

        self.fields = [
            nextcord.ui.StringSelect(
                options=list(self.__class__.CONSTRUCTOR_OPTIONS.keys()),
                placeholder=f"Constructor {i + 1}"
            ) for i in range(number_of_teams)
        ]
        for field in self.fields:
            print(f"Added field: {field.placeholder}")
            self.add_item(field)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.league.add_constructors()
        await self.on_submit(interaction, self.league)

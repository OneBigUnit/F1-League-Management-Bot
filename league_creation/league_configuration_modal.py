from typing import Optional, Callable, Awaitable

import nextcord

from league import League


class LeagueConfigurationModal(nextcord.ui.Modal):
    def __init__(self, callback: Callable[[nextcord.Interaction, League], Awaitable[None]],
                 logo: Optional[nextcord.message.Attachment]) -> None:
        super().__init__("Initial League Configuration", timeout=None)
        self.logo = logo
        self.on_submit = callback

        self.name = nextcord.ui.TextInput(
            label="League Name",
            placeholder="Enter your league's name here...",
            min_length=1,
            max_length=50,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="League Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Enter your league's description here...",
            required=False,
            max_length=4_000,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        logo_url = None if self.logo is None else self.logo.url
        await self.on_submit(interaction, League(self.name.value, self.description.value, logo=logo_url))

from typing import Optional

import nextcord
from nextcord.ext import commands

from league import League, Drivers, Constructors
from league_creation import LeagueConfigurationModal, LeagueConstructorModal

NEW_LEAGUE_COMMAND_DESCRIPTION = (
    """
    Create a league
    """.strip("\n")
)

ADD_CONSTRUCTOR_COMMAND_DESCRIPTION = (
    """
    Add a custom constructor
    """.strip("\n")
)

ADD_DRIVER_COMMAND_DESCRIPTION = (
    """
    Add a custom driver
    """.strip("\n")
)

CONSTRUCTORS_PREBUILT_TYPE = nextcord.SlashOption(
    required=False, choices=[str(c.value) for c in Constructors], name="Prebuilt Constructor", default=None,
    description="Select or prebuilt constructor, or leave this field to add a custom constructor"
)
DRIVERS_PREBUILT_TYPE = nextcord.SlashOption(
    required=False, choices=[str(d.value) for d in Drivers], name="Prebuilt Driver", default=None,
    description="Select or prebuilt driver, or leave this field to add a custom driver"
)


class LeagueSetup(commands.Cog, name="LeagueSetup"):
    def __init__(self, bot: nextcord.ext.commands.bot.Bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="create", description=NEW_LEAGUE_COMMAND_DESCRIPTION)
    async def create_league(self, interaction: nextcord.Interaction,
                            logo: Optional[nextcord.message.Attachment] = None) -> None:
        async def callback(_: nextcord.Interaction, league: League) -> None:
            self.league = league
        modal = LeagueConfigurationModal(callback, logo)
        await interaction.response.send_modal(modal)

    @nextcord.slash_command(name="add_constructor", description=ADD_CONSTRUCTOR_COMMAND_DESCRIPTION)
    async def add_constructor(self, interaction: nextcord.Interaction,
                              prebuilt: Optional[str] = CONSTRUCTORS_PREBUILT_TYPE):
        await interaction.send(str(prebuilt))
        await interaction.send(type(prebuilt))

    @nextcord.slash_command(name="add_driver", description=ADD_DRIVER_COMMAND_DESCRIPTION)
    async def add_driver(self, interaction: nextcord.Interaction,
                         prebuilt: Optional[str] = DRIVERS_PREBUILT_TYPE):
        await interaction.send(str(prebuilt))
        await interaction.send(type(prebuilt))

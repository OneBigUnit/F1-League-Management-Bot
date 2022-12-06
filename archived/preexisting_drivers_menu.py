from archived.options_menu import OptionsMenu
from .option import Option
import discord
from league import Drivers


class PreExistingDriversMenu(OptionsMenu):
    def __init__(self, bot):
        options = [Option(f"Driver {i + 1}", str(driver.value), driver.value) for i, driver in enumerate(Drivers)]
        super().__init__(bot, "Step 3", "Pre-Existing Driver Selection", discord.Colour.blue(), options, inline=True)

    async def prompt(self, ctx):
        return await super().prompt(ctx)

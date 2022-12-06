from archived.multi_select_menu import MultiSelectMenu
import discord
from .multi_select_entry import MultiSelectEntry


class DriverAssignmentMenu(MultiSelectMenu):
    def __init__(self, bot, drivers, constructors):
        entries = [MultiSelectEntry(driver, str(driver), constructors) for driver in drivers]
        super().__init__(bot, "Step 6", "Driver Assignment", discord.Colour.blue(), entries)

    async def prompt(self, ctx):
        return await super().prompt(ctx)

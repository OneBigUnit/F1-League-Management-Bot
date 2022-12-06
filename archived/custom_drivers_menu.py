from archived.task_control_menu import TaskControlMenu
from utilities import channel_input
from .custom_driver_creation_menu import CustomDriverCreationMenu
import discord


class DriversMenu(TaskControlMenu):
    def __init__(self, bot):
        super().__init__(bot, "Step 2", "Driver Setup", discord.Colour.blue(), self.create, self.delete)
        self.drivers = []

    @TaskControlMenu.stage
    async def create(self):
        sub_menu = CustomDriverCreationMenu(self.bot)
        driver = await sub_menu.prompt(self.ctx)
        self.drivers.append(driver)
        return str(driver)

    @TaskControlMenu.stage
    async def delete(self):
        display_name = (await channel_input(self.bot, self.ctx)).content
        self.drivers = list(filter(lambda driver: str(driver) != display_name, self.drivers))
        return display_name

    async def prompt(self, ctx):
        await super().prompt(ctx)
        return self.drivers

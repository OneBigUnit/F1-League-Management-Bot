from archived.task_menu import TaskMenu
from .stage import Stage
import discord
from league import League
from utilities import channel_input


class ConfigMenu(TaskMenu):
    def __init__(self, bot):
        stages = [
            Stage("Name Your League", "Enter a name for your league below", self.name_f, "Not Determined"),
            Stage("Create a League Logo", "Upload a picture for your league logo below",
                  self.logo_f, "Not Determined", optional=True)
        ]
        super().__init__(bot, "Step 1", "Initial League Configuration", discord.Colour.blue(), stages)
        self.name = None
        self.logo = None

    @TaskMenu.stage
    async def name_f(self):
        self.name = (await channel_input(self.bot, self.ctx)).content
        return self.name

    @TaskMenu.stage
    async def logo_f(self):
        user_input = await channel_input(self.bot, self.ctx)
        self.logo = user_input.attachments[0].url if user_input.attachments else ""
        return self.logo

    async def prompt(self, ctx):
        await super().prompt(ctx)
        return League(self.name, self.logo)

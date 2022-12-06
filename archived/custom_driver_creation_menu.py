from archived.task_menu import TaskMenu
from .stage import Stage
import discord
from league import Contestant
from utilities import channel_input


class CustomDriverCreationMenu(TaskMenu):
    def __init__(self, bot):
        stages = [
            Stage("Provide a Discord @", "Mention the discord member that corresponds to this driver below",
                  self.mention_f, "Not Determined"),
            Stage("Enter a First Name", "Enter the first name of your driver below",
                  self.first_f, "Not Determined"),
            Stage("Enter a Last Name", "Enter the last name of your driver below",
                  self.last_f, "Not Determined"),
            Stage("Provide a Display Name", "Enter the preferred display name of the driver below",
                  self.display_name_f, "Not Determined", optional=True)
        ]
        super().__init__(bot, "Create a Driver", "Enter the details of the driver", discord.Colour.blue(), stages)
        self.mention = None
        self.first = None
        self.last = None
        self.display_name = None

    @TaskMenu.stage
    async def mention_f(self):
        user_input = await channel_input(self.bot, self.ctx)
        self.mention = user_input.mentions[0] if user_input.mentions else ""
        return self.mention.display_name if isinstance(self.mention, discord.Member) else ""

    @TaskMenu.stage
    async def first_f(self):
        self.first = (await channel_input(self.bot, self.ctx)).content
        return self.first

    @TaskMenu.stage
    async def last_f(self):
        self.last = (await channel_input(self.bot, self.ctx)).content
        return self.last

    @TaskMenu.stage
    async def display_name_f(self):
        self.display_name = (await channel_input(self.bot, self.ctx)).content
        return self.display_name

    async def prompt(self, ctx):
        await super().prompt(ctx)
        return Contestant(self.mention, self.first, self.last, display_name=self.display_name)

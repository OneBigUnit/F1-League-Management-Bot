import nextcord
from nextcord.ext import commands


class Administration(commands.Cog, name="Administration"):
    def __init__(self, bot: nextcord.ext.commands.bot.Bot) -> None:
        self.bot = bot

    @commands.command(name="latency", aliases=["ping", "response"])
    async def get_latency(self, interaction: nextcord.Interaction) -> None:
        ...

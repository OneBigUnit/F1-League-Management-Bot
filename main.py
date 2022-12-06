import nextcord
from nextcord.ext import commands
import os
from cogs import Administration, LeagueSetup

DESCRIPTION = (
    """
    A discord bot to manage custom F1 leagues for the F1 22 EA Game.
    """.strip("\n")
)
bot = commands.Bot(command_prefix="f1.", description=DESCRIPTION, intents=nextcord.Intents.all())


@bot.event
async def on_ready() -> None:
    print(f"Bot running as '{bot.user}'. (ID: {bot.user.id})")


def run_bot(_bot: nextcord.ext.commands.bot.Bot) -> None:
    for cog in (Administration, LeagueSetup):
        _bot.add_cog(cog(_bot))
    _bot.run(os.environ.get("SECRET_KEY"))


if __name__ == "__main__":
    run_bot(bot)

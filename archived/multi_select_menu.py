from discord.ext import menus
import discord
from .stage import Stage
import asyncio


class MultiSelectMenu(menus.Menu):
    def __init__(self, bot, title, description, colour, entries):
        super().__init__(delete_message_after=True, timeout=None)
        self.embed = discord.Embed(
            title=title,
            description=description,
            colour=colour
        )
        self.entries = entries
        self.entry_index = 0
        self.option_index = 0
        for entry in entries:
            self.embed.add_field(name=str(entry), value=str(entry.option), inline=False)
        self.embed.set_footer(
            text=f"The currently selected entry is {self.entries[self.entry_index].display_name}...")
        self.bot = bot

    async def complete_stage(self):
        stage = self.stages[self.stage_index]
        stage.is_complete = True
        self.embed.set_field_at(self.stage_index, name=str(stage), value=stage.value, inline=False)
        await self.message.edit(embed=self.embed)
        await self.next_stage()

    async def set_stage(self, index):
        self.stage_index = index
        self.embed.set_footer(text=f"{self.stages[self.stage_index].description}...")
        await self.message.edit(embed=self.embed)

    async def send_initial_message(self, _, channel):
        return await channel.send(embed=self.embed)

    @menus.button(Stage.BACK_EMOJI)
    async def back(self, _):
        index = self.stage_index - 1 if self.stage_index > 0 else 0
        await self.set_stage(index)

    @menus.button(Stage.FORWARD_EMOJI)
    async def forward(self, _):
        await self.next_stage()

    async def next_stage(self):
        index = self.stage_index + 1 if self.stage_index < len(self.stages) - 1 else len(self.stages) - 1
        await self.set_stage(index)

    @menus.button(Stage.TICK_EMOJI)
    async def proceed(self, _):
        self.stop()

    async def prompt(self, ctx):
        await super().start(ctx, wait=True)

from discord.ext import menus
import discord
from .control_stage import ControlStage
import asyncio
import functools


class TaskControlMenu(menus.Menu):
    def __init__(self, bot, title, description, colour, on_create, on_delete, empty_key="There are no entries yet",
                 empty_value="Add the first one with the reactions below!"):
        super().__init__(delete_message_after=True, timeout=None)
        self.embed = discord.Embed(
            title=title,
            description=description,
            colour=colour
        )
        self.create_entry = ControlStage("Adding a new entry...", on_create, self.create_entry_f)
        self.delete_entry = ControlStage("Enter the name of an entry from above to delete it", on_delete,
                                         self.delete_entry_f)
        self.empty_key = empty_key
        self.empty_value = empty_value
        self.embed.add_field(name=self.empty_key, value=self.empty_value, inline=False)
        self.bot = bot
        self.task = None
        self.entries = []
        self.active_stage = None

    async def send_initial_message(self, _, channel):
        return await channel.send(embed=self.embed)

    async def set_stage(self, stage):
        self.active_stage = stage
        self.embed.set_footer(text=self.active_stage.description)
        await self.message.edit(embed=self.embed)
        if self.task is not None:
            self.task.cancel()
            await asyncio.sleep(0)
        self.task = asyncio.create_task(self.active_stage())

    @menus.button(ControlStage.CREATE_EMOJI)
    async def create_entry(self, _):
        await self.set_stage(self.create_entry)

    async def create_entry_f(self, value):
        if not self.entries:
            self.embed.remove_field(0)
        self.entries.append(value)
        self.embed.add_field(name=f"Entry {len(self.entries)}", value=value, inline=False)
        await self.message.edit(embed=self.embed)

    @menus.button(ControlStage.DELETE_EMOJI)
    async def delete_entry(self, _):
        await self.set_stage(self.delete_entry)

    async def delete_entry_f(self, value):
        index = self.entries.index(value)
        self.entries.remove(value)
        self.embed.remove_field(index)
        if not self.entries:
            self.embed.add_field(name=self.empty_key, value=self.empty_value, inline=False)
        for i, entry in enumerate(self.entries):
            self.embed.set_field_at(index=i, name=f"Entry {i + 1}", value=entry, inline=False)
        await self.message.edit(embed=self.embed)

    @menus.button(ControlStage.TICK_EMOJI)
    async def proceed(self, _):
        if self.entries:
            if self.task is not None:
                self.task.cancel()
                await asyncio.sleep(0)
            self.stop()

    async def prompt(self, ctx):
        await super().start(ctx, wait=True)

    @staticmethod
    def stage(f):
        @functools.wraps(f)
        async def wrapper(self, *args, **kwargs):
            try:
                value = await f(self, *args, **kwargs)
            except asyncio.CancelledError:
                return
            self.task = None
            self.embed.remove_footer()
            if (self.active_stage == self.delete_entry and value not in self.entries) or not value:
                await self.set_stage(self.active_stage)
                return
            await self.active_stage.do_updates(value)
            return value  # Continuity
        return wrapper

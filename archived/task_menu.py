from discord.ext import menus
import discord
from .stage import Stage
import asyncio
import functools


class TaskMenu(menus.Menu):
    def __init__(self, bot, title, description, colour, stages):
        super().__init__(delete_message_after=True, timeout=None)
        self.embed = discord.Embed(
            title=title,
            description=description,
            colour=colour
        )
        self.stages = stages
        self.stage_index = 0
        for stage in self.stages:
            self.embed.add_field(name=str(stage), value=stage.value, inline=False)
        self.embed.set_footer(text=f"{self.stages[self.stage_index].description}...")
        self.bot = bot
        self.task = asyncio.create_task(self.stages[self.stage_index]())

    async def complete_stage(self):
        stage = self.stages[self.stage_index]
        stage.is_complete = True
        self.embed.set_field_at(self.stage_index, name=str(stage), value=stage.value, inline=False)
        try:
            await self.message.edit(embed=self.embed)
        except discord.errors.NotFound as e:  # TODO: What is the cause here?
            print(f"LOGGED KNOWN ERROR: {e}")
        await self.next_stage()

    async def set_stage(self, index):
        self.stage_index = index
        self.embed.set_footer(text=f"{self.stages[self.stage_index].description}...")
        await self.message.edit(embed=self.embed)
        if self.task is not None:
            self.task.cancel()
            await asyncio.sleep(0)
        self.task = asyncio.create_task(self.stages[self.stage_index]())

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
        if all(stage.optional or stage.is_complete for stage in self.stages):
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
                result = await f(self, *args, **kwargs)
            except asyncio.CancelledError:
                return
            self.task = None
            if not result:
                await self.set_stage(self.stage_index)
                return
            self.stages[self.stage_index].value = result
            await self.complete_stage()
            return result  # Continuity
        return wrapper

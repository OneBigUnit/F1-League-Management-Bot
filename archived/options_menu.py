from discord.ext import menus
import discord
from .option import Option


class OptionsMenu(menus.Menu):
    action = menus.button

    def __init__(self, bot, title, description, colour, options, inline=False):
        super().__init__(delete_message_after=True, timeout=None)
        self.embed = discord.Embed(
            title=title,
            description=description,
            colour=colour
        )
        self.options = options
        self.option_index = 0
        self.inline = inline
        for option in self.options:
            self.embed.add_field(name=str(option), value=option.display_value, inline=self.inline)
        self.embed.set_footer(
            text=f"The currently toggleable option is {self.options[self.option_index].display_value}...")
        self.bot = bot

    async def toggle_option(self):
        option = self.options[self.option_index]
        option.is_selected = not option.is_selected
        self.embed.set_field_at(self.option_index, name=str(option), value=option.display_value, inline=self.inline)
        await self.message.edit(embed=self.embed)
        await self.next_option()

    async def set_option(self, index):
        self.option_index = index
        self.embed.set_footer(
            text=f"The currently toggleable option is {self.options[self.option_index].display_value}...")
        await self.message.edit(embed=self.embed)

    async def send_initial_message(self, _, channel):
        return await channel.send(embed=self.embed)

    @menus.button(Option.BACK_EMOJI)
    async def back(self, _):
        index = self.option_index - 1 if self.option_index > 0 else len(self.options) - 1
        await self.set_option(index)

    @menus.button(Option.FORWARD_EMOJI)
    async def forward(self, _):
        await self.next_option()

    async def next_option(self):
        index = self.option_index + 1 if self.option_index < len(self.options) - 1 else 0
        await self.set_option(index)

    @menus.button(Option.TOGGLE_EMOJI)
    async def toggle(self, _):
        await self.toggle_option()

    @menus.button(Option.TICK_EMOJI)
    async def proceed(self, _):
        self.stop()

    async def prompt(self, ctx):
        await super().start(ctx, wait=True)
        return list(map(lambda option: option.value, filter(lambda option: option.is_selected, self.options)))

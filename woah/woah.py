#!/usr/bin/python3

import discord
from discord.ext import commands


class Woah:
    """Test cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def woah(self):
        """Woah woah woah woah woah!"""

        await self.bot.say(":woah::woah::woah::woah::woah:")


def setup(bot):
    bot.add_cog(Woah(bot))

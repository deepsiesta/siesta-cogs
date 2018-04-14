import discord
from discord.ext import commands
from sympy import preview

class Tex:
    """Renders a LaTeX string"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tex(self, ctx, message):
        """Activate nerd mode"""
        channel = ctx.message.channel
        preview(message, viewer='file', filename='output.png')
        with open('output.png') as f:
            await self.bot.send_file(channel,f)

def setup(bot):
    bot.add_cog(Tex(bot))
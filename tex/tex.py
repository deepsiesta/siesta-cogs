import discord
from discord.ext import commands
from sympy import preview

class Tex:
    """Renders a LaTeX string"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def tex(self, ctx, *, latex):
        """Renders a provided LaTeX string, e.g. !tex $$e^{i\pi}+1=0$$"""
        channel = ctx.message.channel
        preview(latex, viewer='file', filename='output.png')
        with open('output.png','rb') as f:
            await self.bot.send_file(channel,f)

def setup(bot):
    bot.add_cog(Tex(bot))
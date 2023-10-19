import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



def setup(bot: commands.Bot) -> None:
    bot.add_cog(moderation(bot))
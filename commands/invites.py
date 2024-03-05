import discord
from discord.ext import commands
from config import bot_color, gear_icon

class invites(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @discord.slash_command(name="delallinvites", description="Delete ALL active server invites", guild_only=True)
    @discord.commands.default_permissions(manage_guild=True)
    async def invites_list(self, ctx) -> None:
        await ctx.defer()
        guild = ctx.guild
        try:
            for invite in await guild.invites():
                await invite.delete()
        except:
            return await ctx.followup.send("Failed to delete server invites.")
        await ctx.respond(f"Deleted all server invites!")




def setup(bot: commands.Bot) -> None:
    bot.add_cog(invites(bot))
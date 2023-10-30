import discord
from discord.ext import commands
import datetime
from config import bot_color, member_icon

class context_member(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @discord.user_command(name="Timeout for 3 days", guild_only=True)
    @discord.commands.default_permissions(moderate_members=True)
    async def context_timeout(self, ctx: commands.Context, member: discord.Member) -> None:
        days = 3
        duration = datetime.timedelta(days=days)

        if member == ctx.author:
            return await ctx.respond(f"You can't timeout yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("Nuh uh!", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been timed out!", description=f"**Duration:** {days} minutes", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member timed out", icon_url=member_icon)
        embed.set_thumbnail(url=member.avatar)

        try:
            await member.timeout_for(duration, reason=f"timed out by @{ctx.author.name}")
        except:
            await ctx.respond(f"Can't time out {member.mention}! Probably missing permissions, or you're trying to time out someone higher than me", ephemeral=True)

        await ctx.respond(embed=embed)



def setup(bot: commands.Bot) -> None:
    bot.add_cog(context_member(bot))
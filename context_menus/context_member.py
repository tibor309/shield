import datetime
import discord
from discord.ext import commands

from config import bot_color
from config import member_icon


class context_member(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @discord.user_command(name="Timeout for 3 days", guild_only=True)
    @discord.commands.default_permissions(moderate_members=True)
    async def context_timeout(self, ctx, member: discord.Member) -> None:
        days = 3
        duration = datetime.timedelta(days=days)

        if member == ctx.author:
            return await ctx.respond("You can't timeout yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("Nuh uh!", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been timed out!", description=f"**Duration:** {days} minutes", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member timed out", icon_url=member_icon)
        embed.set_thumbnail(url=member.display_avatar)

        try:
            await member.timeout_for(duration, reason=f"timed out by @{ctx.author.name}")
        except:
            await ctx.respond(f"Can't time out {member.mention}! Probably missing permissions, or you're trying to time out someone higher than me", ephemeral=True)

        await ctx.respond(embed=embed)


    
    @discord.user_command(name="Softban", guild_only=True)
    @discord.commands.default_permissions(ban_members=True)
    async def context_softban(self, ctx, member: discord.Member) -> None:
        create_time = int(member.created_at.timestamp())
        join_time = int(member.joined_at.timestamp())

        if member == ctx.author:
            return await ctx.respond("You can't softban yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("Nope", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been softbanned!", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member softbanned", icon_url=member_icon)
        embed.add_field(name="Account Created", value=f"<t:{create_time}:R>")
        embed.add_field(name="Joined Server", value=f"<t:{join_time}:R>")
        embed.set_thumbnail(url=member.display_avatar)

        try:
            await member.ban(reason=f"softbanned by @{ctx.author.name}", delete_message_seconds=604800)
            await member.unban(reason=f"softbanned by @{ctx.author.name}")
        except:
            return await ctx.respond(f"Failed to softban {member.mention}! Probably missing permissions, or you're trying to softban someone higher than me", ephemeral=True)

        await ctx.respond(embed=embed)



def setup(bot: commands.Bot) -> None:
    bot.add_cog(context_member(bot))
    
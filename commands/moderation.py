import discord
from discord.ext import commands
from config import bot_color, member_icon

class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @discord.slash_command(name="kick", description="Kick a member", guild_only=True)
    @discord.commands.default_permissions(kick_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("reason", str, description="Add a reason (optional)", required=False)
    async def ban(self, ctx: commands.Context, member: discord.Member, reason: str = "*no reason given*") -> None:
        create_time = int(member.created_at.timestamp())
        join_time = int(member.joined_at.timestamp())

        if member == ctx.author:
            return await ctx.respond(f"You can't kick yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("You can't do that 😑", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been kicked!", description=f"**Reason:**\n{reason}", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member kicked", icon_url=member_icon)
        embed.add_field(name="Account Created", value=f"<t:{create_time}:R>")
        embed.add_field(name="Joined Server", value=f"<t:{join_time}:R>")
        embed.set_thumbnail(url=member.avatar)

        try:
            await member.kick(reason=f"{reason} - kicked by @{ctx.author.name}")
            await ctx.respond(embed=embed)
        except:
            await ctx.respond(f"Can't kick {member.mention}! Probably missing permissions, or you're trying to kick someone higher than me", ephemeral=True)



def setup(bot: commands.Bot) -> None:
    bot.add_cog(moderation(bot))
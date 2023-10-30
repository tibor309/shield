import discord
from discord.ext import commands
from config import bot_color, member_icon

class member(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @discord.slash_command(name="nickname", description="Change nickname of a member", guild_only=True)
    @discord.commands.default_permissions(manage_nicknames=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("nickname", str, description="Add new nickname", required=True)
    @discord.option("reason", str, description="Add a reason (optional)", required=False)
    async def nickname(self, ctx: commands.Context, member: discord.Member, nickname: str, reason: str = "*No reason given*") -> None:
        embed = discord.Embed(color=bot_color, title=f"Changed nickname for {member.name}", description=f"**Reason:**\n{reason}", timestamp=discord.utils.utcnow())
        embed.set_author(name="Changed nickname", icon_url=member_icon)
        embed.add_field(name="Old nick", value=f"{member.nick}")
        embed.add_field(name="New new", value=f"{nickname}")
        embed.set_thumbnail(url=member.avatar)

        try:
            await member.edit(nick=nickname, reason=f"{reason} - executed by @{ctx.author.name}")
            await ctx.respond(embed=embed)
        except:
            await ctx.respond(f"Failed change nickname for {member.mention}!", ephemeral=True)



    @discord.slash_command(name="deafen", description="Server deafen a member", guild_only=True)
    @discord.commands.default_permissions(deafen_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("state", bool, description="Toggle deafen", required=True)
    async def deafen(self, ctx: commands.Context, member: discord.Member, state: bool) -> None:
        if member == ctx.author:
            return await ctx.respond(f"You can't server deafen yourself!", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("you can't do that", ephemeral=True)

        try:
            if state == True:
                await member.edit(deafen=True, reason=f"executed by @{ctx.author.name}")
                await ctx.respond(f"Server deafened {member.mention}", ephemeral=True)

            elif state == False:
                await member.edit(deafen=False, reason=f"executed by @{ctx.author.name}")
                await ctx.respond(f"Undeafened {member.mention}", ephemeral=True)
        except:
            return await ctx.respond(f"Failed to server un/deafen {member.mention}.", ephemeral=True)



def setup(bot: commands.Bot) -> None:
    bot.add_cog(member(bot))
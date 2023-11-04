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
        except:
            return await ctx.respond(f"Failed to change nickname for {member.mention}! Probably missing permissions.", ephemeral=True)
        await ctx.respond(embed=embed)



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



    @discord.slash_command(name="mute", description="Server mute a member", guild_only=True)
    @discord.commands.default_permissions(mute_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("state", bool, description="Toggle mute", required=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, state: bool) -> None:
        if member == ctx.author:
            return await ctx.respond(f"You can't server mute yourself!", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("you can't do that", ephemeral=True)

        try:
            if state == True:
                await member.edit(mute=True, reason=f"executed by @{ctx.author.name}")
                await ctx.respond(f"Server muted {member.mention}", ephemeral=True)

            elif state == False:
                await member.edit(mute=False, reason=f"executed by @{ctx.author.name}")
                await ctx.respond(f"Unmuted {member.mention}", ephemeral=True)
        except:
            return await ctx.respond(f"Failed to server un/mute {member.mention}.", ephemeral=True)



    @discord.slash_command(name="memberinfo", description="Get info about a member")
    @discord.option("member", discord.Member, description="Select someone", required=True)
    async def member_info(self, ctx: commands.Context, member: discord.Member) -> None:
        creation_time = int(member.created_at.timestamp())
        join_time = int(member.joined_at.timestamp())
    
        embed = discord.Embed(color=bot_color)
        embed.set_thumbnail(url=member.avatar)
        embed.set_author(name="Member info", icon_url=member_icon)
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="Nickname", value=member.nick, inline=True)
        embed.add_field(name="Status", value=member.status, inline=True)

        embed.add_field(name="Server booster", value=bool(member.premium_since), inline=True)
        embed.add_field(name="Bot", value=member.bot, inline=True)
        embed.add_field(name="User ID", value=f"||{member.id}||", inline=True)
        
        embed.add_field(name="Account created", value=f"<t:{creation_time}:R>", inline=True)
        embed.add_field(name="Joined server", value=f"<t:{join_time}:R>", inline=True)
        await ctx.respond(embed=embed)



def setup(bot: commands.Bot) -> None:
    bot.add_cog(member(bot))
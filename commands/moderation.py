import datetime
import discord
from discord.ext import commands

from config import bot_color
from config import member_icon


class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @discord.slash_command(name="kick", description="Kick a member", guild_only=True)
    @discord.commands.default_permissions(kick_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("reason", str, description="Add a reason (optional)", required=False)
    async def kick(self, ctx, member: discord.Member, reason: str = "*No reason given*"):
        create_time = int(member.created_at.timestamp())
        join_time = int(member.joined_at.timestamp())

        if member == ctx.author:
            return await ctx.respond("You can't kick yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("You can't do that 😑", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been kicked!", description=f"**Reason:**\n{reason}", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member kicked", icon_url=member_icon)
        embed.add_field(name="Account Created", value=f"<t:{create_time}:R>")
        embed.add_field(name="Joined Server", value=f"<t:{join_time}:R>")
        embed.set_thumbnail(url=member.display_avatar)

        try:
            await member.kick(reason=f"{reason} - kicked by @{ctx.author.name}")
        except:
            await ctx.respond(f"Can't kick {member.mention}! Probably missing permissions, or you're trying to kick someone higher than me", ephemeral=True)
        await ctx.respond(embed=embed)



    @discord.slash_command(name="ban", description="Ban a member", guild_only=True)
    @discord.commands.default_permissions(ban_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("reason", str, description="Add a reason (optional)", required=False)
    async def ban(self, ctx, member: discord.Member, reason: str = "*No reason given*"):
        create_time = int(member.created_at.timestamp())
        join_time = int(member.joined_at.timestamp())

        if member == ctx.author:
            return await ctx.respond("You can't ban yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("I'm not banning myself", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been banned!", description=f"**Reason:**\n{reason}", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member banned", icon_url=member_icon)
        embed.add_field(name="Account Created", value=f"<t:{create_time}:R>")
        embed.add_field(name="Joined Server", value=f"<t:{join_time}:R>")
        embed.set_thumbnail(url=member.display_avatar)

        try:
            await member.ban(reason=f"{reason} - banned by @{ctx.author.name}")
        except:
            return await ctx.respond(f"Can't ban {member.mention}! Probably missing permissions, or you're trying to ban someone higher than me", ephemeral=True)
        await ctx.respond(embed=embed)



    @discord.slash_command(name="softban", description="Softban a member (ban and unban to delete messages)", guild_only=True)
    @discord.commands.default_permissions(ban_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("reason", str, description="Add a reason (optional)", required=False)
    async def softban(self, ctx, member: discord.Member, reason: str = "*No reason given*"):
        create_time = int(member.created_at.timestamp())
        join_time = int(member.joined_at.timestamp())

        if member == ctx.author:
            return await ctx.respond("You can't softban yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("Nope", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been softbanned!", description=f"**Reason:**\n{reason}", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member softbanned", icon_url=member_icon)
        embed.add_field(name="Account Created", value=f"<t:{create_time}:R>")
        embed.add_field(name="Joined Server", value=f"<t:{join_time}:R>")
        embed.set_thumbnail(url=member.display_avatar)

        try:
            await member.ban(reason=f"{reason} - softbanned by @{ctx.author.name}", delete_message_seconds=604800)
            await member.unban(reason=f"{reason} - softbanned by @{ctx.author.name}")
        except:
            return await ctx.respond(f"Failed to softban {member.mention}! Probably missing permissions, or you're trying to softban someone higher than me", ephemeral=True)
        await ctx.respond(embed=embed)



    @discord.slash_command(name="timeout", description="Timeout a member", guild_only=True)
    @discord.commands.default_permissions(moderate_members=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("minutes", int, description="Timeout duration", required=True)
    @discord.option("reason", str, description="Add a reason (optional)", required=False)
    async def timeout(self, ctx, member: discord.Member, minutes: int, reason: str = "*No reason given*"):
        duration = datetime.timedelta(minutes=minutes)

        if member == ctx.author:
            return await ctx.respond(f"You can't timeout yourself", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("Nuh uh!", ephemeral=True)

        embed = discord.Embed(color=bot_color, title=f"{member.name} has been timed out!", description=f"**Duration:** {minutes} minutes\n**Reason:** {reason}", timestamp=discord.utils.utcnow())
        embed.set_author(name="Member timed out", icon_url=member_icon)
        embed.set_thumbnail(url=member.display_avatar)

        try:
            await member.timeout_for(duration, reason=f"{reason} - timed out by @{ctx.author.name}")
        except:
            return await ctx.respond(f"Can't timeout {member.mention}! Probably missing permissions, or you're trying to time out someone higher than me", ephemeral=True)
        await ctx.respond(embed=embed)



    @discord.slash_command(name="rolegive", description="Give a role to a member", guild_only=True)
    @discord.commands.default_permissions(manage_roles=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("role", discord.Role, description="Select a role", required=True)
    async def rolegive(self, ctx, member: discord.Member, role: discord.Role):
        if member == ctx.author:
            return await ctx.respond(f"You can't give yourself roles!", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("You can't do that.", ephemeral=True)

        try:
            await member.add_roles(role, reason=f"added role by @{ctx.author.name}")
        except:
            return await ctx.respond(f"Failed to give role. Probably a higher role than mine, or {member.mention} already has that role", ephemeral=True)
        await ctx.respond(f"Added the {role.mention} role to {member.mention}", ephemeral=True)



    @discord.slash_command(name="rolerevoke", description="Revoke a role from a member", guild_only=True)
    @discord.commands.default_permissions(manage_roles=True)
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("role", discord.Role, description="and select a role", required=True)
    async def revoke_role(self, ctx, member: discord.Member, role: discord.Role):
        if member == ctx.author:
            return await ctx.respond(f"You can't revoke roles from yourself!", ephemeral=True)
        elif member == self.bot.user:
            return await ctx.respond("You can't do that.", ephemeral=True)

        try:
            await member.remove_roles(role, reason=f"removed role by @{ctx.author.name}")
        except:
            return await ctx.respond(f"Failed to remove role. Probably a higher role than mine, or {member.mention} doesn't have that role.", ephemeral=True)
        await ctx.respond(f"Removed the {role.mention} role from {member.mention}", ephemeral=True)



def setup(bot: commands.Bot):
    bot.add_cog(moderation(bot))
    
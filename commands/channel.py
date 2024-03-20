import discord
from discord.ext import commands


class channel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @discord.slash_command(name="lock", description="Lock or unlock a channel", guild_only=True)
    @discord.commands.default_permissions(manage_channels=True)
    @discord.option("channel", discord.TextChannel, description="Select a channel if you want too", required=True)
    @discord.option("state", bool, description="Toggle channel lock", required=True)
    async def channel_lock(self, ctx, channel: discord.TextChannel, state: bool):
        try:
            if state == True:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True, reason=f"executed by @{ctx.author.name}")
                await ctx.respond(f"Locked {channel.mention}")

            elif state == False:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False, reason=f"executed by @{ctx.author.name}")
                await ctx.respond(f"Unlocked {channel.mention}")
        except:
            return await ctx.respond("I don't have access to that channel", ephemeral=True)



def setup(bot: commands.Bot):
    bot.add_cog(channel(bot))
    
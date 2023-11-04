import discord
from discord.ext import commands
from asyncio import sleep

class messages(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @discord.slash_command(name="clear", description="Delete messages", guild_only=True)
    @discord.commands.default_permissions(manage_messages=True)
    @discord.option("messages", int, description="Number of messages", required=True)
    async def clear(self, ctx: commands.Context, messages: int) -> None:
        await ctx.defer(ephemeral=True)

        try:
            await ctx.channel.purge(limit=messages)
            await sleep(1)
            await ctx.followup.send(f"Deleted {messages} messages")
        except:
            return await ctx.followup.send("Failed to delete messages! Check if i have the correct permissions.", ephemeral=True)



def setup(bot: commands.Bot) -> None:
    bot.add_cog(messages(bot))
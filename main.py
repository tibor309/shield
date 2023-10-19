import discord
from discord.ext import commands
from config import bot_token

intents = discord.Intents.default()
bot = commands.Bot(intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}")


# Make bot not respond to it's owm messages
@bot.listen
async def on_message(message):
    if message.author == bot.user:
        return

bot.run(bot_token)

# TODO:
# moderation commands (kick, ban, etc.)
# timeout members
# purge messages
# give/revoke roles
# delete server invites
# lock/unlock channel
# set nickname for a member
# softban members
# un/deafen members
# mute members
# member info
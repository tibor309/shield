import discord
from discord.ext import commands
import os
from config import bot_time, bot_token

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(intents=intents, help_command=None)

# load commands
for f in os.listdir("./commands"):
    if f.endswith(".py"):
        #try:
            bot.load_extension("commands." + f[:-3])
        #except Exception as error:
            #print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"ERROR {f} could not be loaded: {error}")
        #else:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded {f}")

for f in os.listdir("./context_menus"):
    if f.endswith(".py"):
        #try:
            bot.load_extension("context_menus." + f[:-3])
        #except Exception as error:
            #print((discord.utils.utcnow().strftime(f"[{bot_time}]")), f"ERROR {f} could not be loaded: {error}")
        #else:
            print((discord.utils.utcnow().strftime(f"[{bot_time}]")),f"Loaded {f}")

# sync commands
@bot.event
async def on_connect():
    await bot.sync_commands(delete_existing=True)
    print((discord.utils.utcnow().strftime(f"[{bot_time}]")), "Synced commands")

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
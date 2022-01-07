import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from ext import music
from ext import help_music

load_dotenv()
music_cogs = [music]
help_cogs = [help_music]
client = commands.Bot(command_prefix=("1!", "-"), intents = discord.Intents.all(), help_command=None)

@client.event
async def on_ready():
    print("{0.user} successful log in! ".format(client))
    await client.change_presence(activity=discord.Game("Receptionist"))

for i in range(len(music_cogs)):
    music_cogs[i].setup(client)

for i in range(len(help_cogs)):
    help_cogs[i].setup(client)


client.run(os.getenv("TOKEN"))
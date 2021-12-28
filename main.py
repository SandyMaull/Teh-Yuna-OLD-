import discord
from discord.ext import commands


client = commands.Bot(command_prefix='?!', intents = discord.Intents.all())
@client.event
async def on_ready():
    print("{0.user} successful log in! ".format(client))
    await client.change_presence(activity=discord.Game("Receptionist"))


client.run("OTI1MTcxODY0MjI4MjA0NTY1.YcpPcQ.uU9dBzdNM-jWKS5d2HeqdRH2TWU")
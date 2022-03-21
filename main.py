import discord
from discord.ext import commands
import music
import fun
import os

cogs = [music, fun]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(os.environ['TOKEN'])
